#!/usr/bin/python

import logging
class NullHandler(logging.Handler):
    def emit(self, record):
        pass
log = logging.getLogger('NetworkStateAnalyzer')
log.setLevel(logging.ERROR)
log.addHandler(NullHandler())

import inspect
import threading

from   DustLinkData import DustLinkData
from   EventBus     import EventBusClient
from   SmartMeshSDK import FormatUtils

class NetworkStateAnalyzer(EventBusClient.EventBusClient):
    
    QUEUESIZE           = 100
    
    def __init__(self,connectParams):
        
        # log
        log.info("creating instance")
        
        # store params
        self.connectParams        = connectParams
        
        # local variables
        self.netname              = FormatUtils.formatConnectionParams(self.connectParams)
        self.busyTesting          = threading.Lock()
        
        # initialize parent class
        EventBusClient.EventBusClient.__init__(self,
            signal                = 'snapShotEnd_{0}'.format(self.netname),
            cb                    = self._ebHandler_snapShotEnd,
            teardown_cb           = self._cleanup,
            queuesize             = self.QUEUESIZE,
        )
        self.name                 = '{0}_NetworkStateAnalyzer'.format(self.netname)
    
    def _cleanup(self):
        pass
    
    #======================== public ==========================================
    
    #======================== eventBus handlers ===============================
    
    #===== snapShotEnd
    
    def _ebHandler_snapShotEnd(self,sender,signal,data):
        
        dld = DustLinkData.DustLinkData()
        
        testsFailed = False
        
        # discover and run all the network tests
        with self.busyTesting:
            for f in dir(self):
                
                if f.startswith("_nettest_"):
                    
                    # execute the test
                    (outcome,description) = getattr(self,f)()
                    assert outcome in dld.TEST_OUTCOME_ALL
                    assert type(description)==str
                    
                    # remember if test failed
                    if outcome==dld.TEST_OUTCOME_FAIL:
                        testsFailed = True 
                    
                    # log
                    if log.isEnabledFor(logging.DEBUG):
                        log.debug('testResult outcome={0} description={1}'.format(outcome,description))
                    
                    # dispatch
                    self._dispatch(
                        signal           = 'testResult_{0}'.format(self.netname),
                        data             = {
                            'testName':       f,
                            'testDesc':       getattr(self,f).__doc__,
                            'outcome':        outcome,
                            'description':    description,
                        },
                    )
        
        # write to banner if tests failed
        if testsFailed:
            dld._setBanner(
                'some tests failed for network <a href="/health/_{0}">{1}</a>'.format(
                    FormatUtils.quote(self.netname),
                    self.netname
                )
            )
    
    #======================== network tests ===================================
    
    #===== network availability
    
    MIN_NETWORKAVAILABILITY = 0.99
    
    def _nettest_networkAvailability(self):
        '''
        <p>
            This test verifies that the overall network availability is above 
            MIN_NETWORKAVAILABILITY.
        </p>
        <p>
            The network availability is the portion of the packets generated by
            the motes' apps, which were actually sent into the network. If the
            protocol stack is busy, it will reject the application's data,
            resulting in a lower availability.
        </p>
        <p>
            This test is run once for the whole network.
        </p>
        '''
        
        dld                  = DustLinkData.DustLinkData()
        
        descPASS             = []
        descFAIL             = []
        descNOTRUN           = []
        
        # counter network-wide number of packets generated/failed
        numTxOk              = 0
        numTxFail            = 0
        for mac in dld.getNetworkMotes(self.netname):
            moteinfo = dld.getMoteInfo(mac)
            if (('numTxOk' in moteinfo) and ('numTxFail' in moteinfo)):
                numTxOk     += moteinfo['numTxOk']
                numTxFail   += moteinfo['numTxFail']
        
        # stop here if both counters are 0
        if not numTxOk:
            descNOTRUN      += ['This test could not run because no packets were sent in the network (yet?) (numTxOk=={0} for the network) and so it is impossible to calculate a ratio.'.format(numTxOk)]
        
        if not descNOTRUN:
        
            # calculate resulting network availability
            networkAvailability  = (1-float(numTxFail)/float(numTxOk))
            
            # make sure about threshold
            if (networkAvailability>=self.MIN_NETWORKAVAILABILITY):
                descPASS    += [
                    'networkAvailability={0} is better than the expected {1}'.format(
                        networkAvailability,
                        self.MIN_NETWORKAVAILABILITY
                    )
                ]
            else:
                descFAIL    += [
                    'networkAvailability={0} is below the expected {1}'.format(
                        networkAvailability,
                        self.MIN_NETWORKAVAILABILITY
                    )
                ]
        
        # decide outcome and write report
        if   descNOTRUN:
            outcome          = dld.TEST_OUTCOME_NOTRUN
            description      = ''.join(descNOTRUN)
        elif descPASS:
            outcome          = dld.TEST_OUTCOME_PASS
            description      = ''.join(descPASS)
        elif descFAIL:
            outcome          = dld.TEST_OUTCOME_FAIL
            description      = ''.join(descFAIL)
        
        # return test result
        return (outcome,description)
    
    #===== network reliability
    
    MIN_NETWORKRELIABILITY = 0.999
    
    def _nettest_networkReliability(self):
        '''
        <p>
            This test erifies that the overall network reliability is above 
            MIN_NETWORKRELIABILITY.
        </p>
        <p>
            The network reliability is the portion of the packets injected into
            the network that were received by their final destination. If the
            network looses data, the network reliability goes down.
        </p>
        <p>
            This test is run once for the whole network.
        </p>
        '''
        
        dld                  = DustLinkData.DustLinkData()
        
        descPASS             = []
        descFAIL             = []
        descNOTRUN           = []
        
        # counter network-wide number of packets generated/lost
        numPktsGenerated     = 0
        numPktsLost          = 0
        for mac in dld.getNetworkMotes(self.netname):
            moteinfo = dld.getMoteInfo(mac)
            if ('packetsReceived' in moteinfo):
                numPktsGenerated += moteinfo['packetsReceived']
            if ('packetsLost' in moteinfo):
                numPktsGenerated += moteinfo['packetsLost']
        
        # stop here if both counters are 0
        if (not numPktsGenerated) and (not numPktsLost):
            descNOTRUN      += [
                'This test could not run because numPktsGenerated=={0} and numPktsLost=={1} and so its\'s impossible to calculate a ratio.'.format(
                    numPktsGenerated,
                    numPktsLost,
                )
            ]
        
        if not descNOTRUN:
        
            # calculate resulting network reliability
            networkReliability    = (1-float(numPktsLost)/float(numPktsLost + numPktsGenerated))
            
            # make sure about threshold
            if (networkReliability>=self.MIN_NETWORKRELIABILITY):
                descPASS    += [
                    'networkReliability={0} is better than the expected {1}'.format(
                        networkReliability,
                        self.MIN_NETWORKRELIABILITY,
                    )
                ]
            else:
                descFAIL    += [
                    'networkAvailability={0} is below the expected {1}'.format(
                        networkAvailability,
                        self.MIN_NETWORKAVAILABILITY,
                    )
                ]
        
        # decide outcome and write report
        if   descNOTRUN:
            outcome          = dld.TEST_OUTCOME_NOTRUN
            description      = ''.join(descNOTRUN)
        elif descPASS:
            outcome          = dld.TEST_OUTCOME_PASS
            description      = ''.join(descPASS)
        elif descFAIL:
            outcome          = dld.TEST_OUTCOME_FAIL
            description      = ''.join(descFAIL)
        
        # return test result
        return (outcome,description)
    
    #===== multiple joins
    
    def _nettest_multipleJoins(self):
        '''
        <p>
            This test verifies that each mote has joined exactly once.
        </p>
        <p>
            In a normal deployment, all motes should join exactly once. Joining
            more than once may indicate a mote reset.
        </p>
        <p>
            This test is run once for each node in the network (both AP and
            mote).
        </p>
        '''
        
        dld                  = DustLinkData.DustLinkData()
        
        descPASS             = []
        descFAIL             = []
        descNOTRUN           = []
        
        # run test
        motesExactlyOnce     = []
        motesNotExactlyOnce  = []
        motesNotRun          = []
        for mac in dld.getNetworkMotes(self.netname):
            moteinfo = dld.getMoteInfo(mac)
            
            if ('numOperationalEvents' in moteinfo):
                if moteinfo['numOperationalEvents']==1:
                    descPASS     += ['- {0} has numOperationalEvents=={1}'.format(
                            FormatUtils.formatMacString(mac),
                            moteinfo['numOperationalEvents'],
                        )
                    ]
                else:
                    descFAIL     += ['- {0} has numOperationalEvents=={1}'.format(
                            FormatUtils.formatMacString(mac),
                            moteinfo['numOperationalEvents'],
                        )
                    ]
            else:
                if (('state' in moteinfo) and (moteinfo['state']==4)):
                    descPASS     += ['- {0} has no numOperationalEvents parameters, but its state is {1}'.format(
                            FormatUtils.formatMacString(mac),
                            moteinfo['state'],
                        )
                    ]
                else:
                    descNOTRUN   += ['- {0} has neither numOperationalEvents, nor state attribute'.format(
                            FormatUtils.formatMacString(mac),
                        )
                    ]
        
        # decide outcome
        if   descFAIL:
            outcome     = dld.TEST_OUTCOME_FAIL
        elif descPASS:
            outcome     = dld.TEST_OUTCOME_PASS
        else:
            outcome     = dld.TEST_OUTCOME_NOTRUN
        
        # write report
        description  = []
        if descPASS:
            description  += ["PASS</b>:"]
            description  += descPASS
        if descFAIL:
            description  += ["FAIL:"]
            description  += descFAIL
        if descNOTRUN:
            description  += ["NOTRUN:"]
            description  += descNOTRUN
        description = '<br/>'.join(description)
        
        # return test result
        return (outcome,description)
    
    #===== number of links
    
    MAX_AP_RXLINKS = 140
    MAX_MOTE_LINKS = 180
    
    def _nettest_numLinks(self):
        '''
        <p>
            This test verifies that the number of links assigned to each mote
            does not exceed the maximum limit.
        </p>
        <p>
            The manager is never supposed to allocate more than MAX_AP_RXLINKS
            receive links to the AP, nor more than MAX_MOTE_LINKS links (both
            transmit and receive) for a non-AP mote.
        </p>
        <p>
            This test is run once for each node in the network (both AP and
            mote).
        </p>
        '''
        
        dld                  = DustLinkData.DustLinkData()
        
        descPASS             = []
        descFAIL             = []
        descNOTRUN           = []
        
        # get all the paths in the network
        currentPaths         = dld.getNetworkPaths(self.netname)
        
        for mac in dld.getNetworkMotes(self.netname):
            
            (numTx,numRx)    = self._countTxRxLinks(currentPaths,mac)
            moteinfo = dld.getMoteInfo(mac)
            
            if moteinfo['isAP']:
                if numRx<self.MAX_AP_RXLINKS:
                    descPASS  += [
                        'AP {0} has {1} RX links, less than maximum {2}'.format(
                            FormatUtils.formatMacString(mac),
                            numRx,
                            self.MAX_AP_RXLINKS
                        )
                    ]
                else:
                    descFAIL  += [
                        'AP {0} has {1} RX links, more than maximum {2}'.format(
                            FormatUtils.formatMacString(mac),
                            numRx,
                            self.MAX_AP_RXLINKS
                        )
                    ]
            else:
                numLinks = numTx+numRx
                if numLinks<self.MAX_MOTE_LINKS:
                    descPASS  += [
                        'mote {0} has {1} links, less than maximum {2}'.format(
                            FormatUtils.formatMacString(mac),
                            numLinks,
                            self.MAX_MOTE_LINKS
                        )
                    ]
                else:
                    descFAIL  += [
                        'mote {0} has {1} links, more than maximum {2}'.format(
                            FormatUtils.formatMacString(mac),
                            numLinks,
                            self.MAX_MOTE_LINKS
                        )
                    ]
        
        # decide outcome
        if   descFAIL:
            outcome     = dld.TEST_OUTCOME_FAIL
        elif descPASS:
            outcome     = dld.TEST_OUTCOME_PASS
        else:
            outcome     = dld.TEST_OUTCOME_NOTRUN
        
        # write report
        description  = []
        if descPASS:
            description  += ["PASS:"]
            description  += descPASS
        if descFAIL:
            description  += ["FAIL:"]
            description  += descFAIL
        if descNOTRUN:
            description  += ["NOTRUN:"]
            description  += descNOTRUN
        description = '<br/>'.join(description)
        
        # return test result
        return (outcome,description)
    
    def _countTxRxLinks(self,paths,mac):
        
        numTx           = 0
        numRx           = 0
        
        dld = DustLinkData.DustLinkData()
        
        for (fromMote,toMote) in paths:
            
            if mac!=fromMote and mac!=toMote:
                continue
            
            pathInfo = dld.getPathInfo(self.netname,fromMote,toMote)
            
            if mac==fromMote:
                numTx  += pathInfo['numLinks']
            if mac==toMote:
                numRx  += pathInfo['numLinks']
        
        return (numTx,numRx)
    
    #===== number of good neighbors
    
    MIN_NUMGOODNEIGHBORS = 3
    
    def _nettest_numGoodNeighbors(self):
        '''
        <p>
            This test verifies that each mote has enough good neighbors.
        </p>
        <p>
            The manager can build a robust network if each mote in the network
            has at least MIN_NUMGOODNEIGHBORS neighbors.
        </p>
        <p>
            This test is run once for each mote in the network.
        </p>
        '''
        
        dld                  = DustLinkData.DustLinkData()
        
        descPASS             = []
        descFAIL             = []
        descNOTRUN           = []
        
        for mac in dld.getNetworkMotes(self.netname):
            
            moteinfo         = dld.getMoteInfo(mac)
            
            if 'numGoodNbrs' not in moteinfo:
                descNOTRUN += [
                    'This test could not run because mote {0} did not report any numGoodNbrs counter (the counters it did report are {1}).'.format(
                        FormatUtils.formatMacString(mac),
                        moteinfo.keys()
                    )
                ]
            elif moteinfo['numGoodNbrs']<self.MIN_NUMGOODNEIGHBORS:
                descFAIL += [
                    'mote {0} has {1} good neighbors, expected at least {2}.'.format(
                        FormatUtils.formatMacString(mac),
                        moteinfo['numGoodNbrs'],
                        self.MIN_NUMGOODNEIGHBORS
                    )
                ]
            else:
                descPASS += [
                    'mote {0} has {1} good neighbors, which is more than {2}.'.format(
                        FormatUtils.formatMacString(mac),
                        moteinfo['numGoodNbrs'],
                        self.MIN_NUMGOODNEIGHBORS
                    )
                ]
        
        # decide outcome
        if   descFAIL:
            outcome     = dld.TEST_OUTCOME_FAIL
        elif descPASS:
            outcome     = dld.TEST_OUTCOME_PASS
        else:
            outcome     = dld.TEST_OUTCOME_NOTRUN
        
        # write report
        description  = []
        if descPASS:
            description  += ["PASS:"]
            description  += descPASS
        if descFAIL:
            description  += ["FAIL:"]
            description  += descFAIL
        if descNOTRUN:
            description  += ["NOTRUN:"]
            description  += descNOTRUN
        description = '<br/>'.join(description)
        
        # return test result
        return (outcome,description)
    
    #===== mote availability
    
    MIN_MOTEAVAILABILITY = 0.99
    
    def _nettest_perMoteAvailability(self):
        '''
        <p>
            This test verifies that the availability for each mote is above 
            MIN_MOTEAVAILABILITY.
        </p>
        <p>
            The mote availability is the portion of the packets generated by
            the mote's application which were actually sent into the network.
            If the mote's protocol stack is busy, it will reject the
            application's data, resulting in a lower availability.
        </p>
        <p>
            This test is run once for each mote in the network.
        </p>
        '''
        
        dld                  = DustLinkData.DustLinkData()
        
        descPASS             = []
        descFAIL             = []
        descNOTRUN           = []
        
        for mac in dld.getNetworkMotes(self.netname):
            
            moteinfo       = dld.getMoteInfo(mac)
            
            #==== filter edge cases where the test can not be run
            
            if ('isAP' in moteinfo) and moteinfo['isAP']==True:
                # don't run test on AP
                continue
            
            if 'numTxOk' not in moteinfo:
                descNOTRUN += [
                    'This test could not run because mote {0} did not report any numTxOk counter (the counters it did report are {1}).'.format(
                        FormatUtils.formatMacString(mac),
                        moteinfo.keys()
                    )
                ]
                continue
                
            if 'numTxFail' not in moteinfo:
                descNOTRUN += [
                    'This test could not run because mote {0} did not report any numTxFail counter (the counters it did report are {1}).'.format(
                        FormatUtils.formatMacString(mac),
                        moteinfo.keys()
                    )
                ]
                continue
            
            if not moteinfo['numTxOk']:
                descNOTRUN += [
                    'This test could not run because mote {0} did not send any packets succesfully (yet?) (numTxOk=={1}) and so its\'s impossible to calculate a ratio.'.format(
                        FormatUtils.formatMacString(mac),
                        moteinfo['numTxOk']
                    )
                ]
                continue
            
            #==== run the test
            
            availability = (1-float(moteinfo['numTxFail'])/float(moteinfo['numTxOk']))
            if availability<self.MIN_MOTEAVAILABILITY:
                descFAIL += [
                    'availability for mote {0} is {1}, expected at least {2}.'.format(
                        FormatUtils.formatMacString(mac),
                        availability,
                        self.MIN_MOTEAVAILABILITY
                    )
                ]
            else:
                descPASS += [
                    'availability for mote {0} is {1}, which is better than {2}.'.format(
                        FormatUtils.formatMacString(mac),
                        availability,
                        self.MIN_MOTEAVAILABILITY
                    )
                ]
        
        # decide outcome
        if   descFAIL:
            outcome     = dld.TEST_OUTCOME_FAIL
        elif descPASS:
            outcome     = dld.TEST_OUTCOME_PASS
        else:
            outcome     = dld.TEST_OUTCOME_NOTRUN
        
        # write report
        description  = []
        if descPASS:
            description  += ["PASS:"]
            description  += descPASS
        if descFAIL:
            description  += ["FAIL:"]
            description  += descFAIL
        if descNOTRUN:
            description  += ["NOTRUN:"]
            description  += descNOTRUN
        description = '<br/>'.join(description)
        
        # return test result
        return (outcome,description)
    
    #===== single single parent
    
    def _nettest_oneSingleParentMote(self):
        '''
        <p>
            This test verifies that there is exactly mote with only one parent.
        </p>
        <p>
            Graph theory indicates that, when building a bi-DAG, exactly one
            node ends up with one parent (it will be a one-hop neighbor of the
            root). This test verifies that this is the case in this network.
        </p>
        <p>
            This test is run once for the whole network.
        </p>
        '''
        
        dld                  = DustLinkData.DustLinkData()
        
        descPASS             = []
        descFAIL             = []
        descNOTRUN           = []
        
        numParents           = {}
        singleParentMotes    = []
        
        # get all the paths in the network
        currentPaths         = dld.getNetworkPaths(self.netname)
        
        # count number of parents for each mote
        for mac in dld.getNetworkMotes(self.netname):
            numParents[mac] = 0
            for (fromMote,toMote) in currentPaths:
                pathInfo = dld.getPathInfo(self.netname,fromMote,toMote)
                if fromMote==mac and pathInfo['direction']==2 and pathInfo['numLinks']>0:
                    numParents[mac] += 1
        
        # count number of single-parents motes
        for (mac,n) in numParents.items():
            if n==1:
                singleParentMotes      = [mac]
        
        # run test
        if len(singleParentMotes)==1:
            descPASS    += [
                'only mote {0} has a single parent'.format(
                    FormatUtils.formatMacString(singleParentMotes[0]),
                )
            ]
        else:
            description  = []
            description += ['The following {0} motes have one parent only: '.format(len(singleParentMotes))]
            description += [' '.join(FormatUtils.formatMacString(m) for m in singleParentMotes)]
            description  = ''.join(description)
            descPASS    += [description]
        
        # decide outcome
        if   descFAIL:
            outcome     = dld.TEST_OUTCOME_FAIL
        elif descPASS:
            outcome     = dld.TEST_OUTCOME_PASS
        else:
            outcome     = dld.TEST_OUTCOME_NOTRUN
        
        # write report
        description  = []
        if descPASS:
            description  += ["PASS:"]
            description  += descPASS
        if descFAIL:
            description  += ["FAIL:"]
            description  += descFAIL
        if descNOTRUN:
            description  += ["NOTRUN:"]
            description  += descNOTRUN
        description = '<br/>'.join(description)
        
        # return test result
        return (outcome,description)
    
    #===== stability vs. RSSI
    
    THRES_NUM_PACKETS   = 30
    THRES_HIGH_RSSI     = -70
    THRES_HIGH_STAB     = 0.70
    THRES_LOW_RSSI      = -80
    THRES_LOW_STAB      = 0.50
    
    def _nettest_stabilityVsRssi(self):
        '''
        <p>
            This test verifies that stability of a path is plausible given its
            RSSI.
        </p>
        <p>
            In the absence of heavy interference, the is a straightforward
            relationship between the RSSI and stability of a path:
            <ul>
                <li>if the RSSI is above THRES_HIGH_RSSI, the stability is
                expected to be above THRES_HIGH_STAB.</li>
                <li>if the RSSI is below THRES_LOW_RSSI, the stability is expected to
                be below THRES_LOW_STAB.</li>
            </ul>
        </p>
        <p>
            The stability is calculated as the ratio between the number of
            packets transmitted successfully and transmission attempts; it is
            also known as Packet Delivery Ratio (PDR).
        </p>
        <p>
            This test is run once for each path in the network over which at
            least THRES_NUM_PACKETS packet have been transmitted.
        </p>
        '''
        
        dld                  = DustLinkData.DustLinkData()
        
        descPASS             = []
        descFAIL             = []
        descNOTRUN           = []
        
        currentPaths         = dld.getNetworkPaths(self.netname)
        
        for (fromMote,toMote) in currentPaths:
            pathInfo = dld.getPathInfo(self.netname,fromMote,toMote)
            
            # make sure path information contains all the counters
            if ('rssi' not in pathInfo) or ('numTxPackets' not in pathInfo) or ('numTxFailures' not in pathInfo):
                continue
            
            # make sure source has sent enough packets to destination
            if pathInfo['numTxPackets']<self.THRES_NUM_PACKETS:
                continue
            
            # calculate link stability and RSSI
            linkStability = 1-float(pathInfo['numTxFailures'])/float(pathInfo['numTxPackets'])
            linkRssi      = pathInfo['rssi']
            
            # test for high RSSI
            if linkRssi>self.THRES_HIGH_RSSI:
                if linkStability>self.THRES_HIGH_STAB:
                    descPASS += [
                        'link {0}->{1} has RSSI {2} (>{3}) and stability {4} (>{5})'.format(
                            FormatUtils.formatMacString(fromMote),
                            FormatUtils.formatMacString(toMote),
                            linkRssi,
                            self.THRES_HIGH_RSSI,
                            linkStability,
                            self.THRES_HIGH_STAB,
                        )
                    ]
                else:
                    descFAIL += [
                        'link {0}->{1} has RSSI {2} (>{3}) and stability {4} (<{5})'.format(
                            FormatUtils.formatMacString(fromMote),
                            FormatUtils.formatMacString(toMote),
                            linkRssi,
                            self.THRES_HIGH_RSSI,
                            linkStability,
                            self.THRES_HIGH_STAB,
                        )
                    ]
            
            # test for low RSSI
            if linkRssi<self.THRES_LOW_RSSI:
                if linkStability<self.THRES_LOW_STAB:
                    descPASS += [
                        'link {0}->{1} has RSSI {2} (<{3}) and stability {4} (<{5})'.format(
                            FormatUtils.formatMacString(fromMote),
                            FormatUtils.formatMacString(toMote),
                            linkRssi,
                            self.THRES_LOW_RSSI,
                            linkStability,
                            self.THRES_LOW_STAB,
                        )
                    ]
                else:
                    descFAIL += [
                        'link {0}->{1} has RSSI {2} (<{3}) and stability {4} (>{5})'.format(
                            FormatUtils.formatMacString(fromMote),
                            FormatUtils.formatMacString(toMote),
                            linkRssi,
                            self.THRES_LOW_RSSI,
                            linkStability,
                            self.THRES_LOW_STAB,
                        )
                    ]
        
        # decide outcome
        if   descFAIL:
            outcome     = dld.TEST_OUTCOME_FAIL
        elif descPASS:
            outcome     = dld.TEST_OUTCOME_PASS
        else:
            outcome     = dld.TEST_OUTCOME_NOTRUN
        
        # write report
        description  = []
        if descPASS:
            description  += ["PASS:"]
            description  += descPASS
        if descFAIL:
            description  += ["FAIL:"]
            description  += descFAIL
        if descNOTRUN:
            description  += ["NOTRUN:"]
            description  += descNOTRUN
        description = '<br/>'.join(description)
        
        # return test result
        return (outcome,description)
    
    '''
    #===== dump info
    
    def _nettest_dumpInfo(self):
        
        # dump moteInfo
        dld = DustLinkData.DustLinkData()
        output = []
        for mac in dld.getNetworkMotes(self.netname):
            moteinfo = dld.getMoteInfo(mac)
            output += ['']
            output += ['{0}:'.format(FormatUtils.formatMacString(mac))]
            for (k,v) in moteinfo.items():
                output += ['- {0}: {1}'.format(k,v)]
        output = '\n'.join(output)
        f = open('poipoi_moteinfo.txt','w')
        f.write(output)
        f.close()
        print 'moteInfo dumped'
        
        # dump pathInfo
        dld = DustLinkData.DustLinkData()
        currentPaths         = dld.getNetworkPaths(self.netname)
        output  = []
        for (fromMote,toMote) in currentPaths:
            output += ['']
            output += ['{0} -> {1}'.format(
                    FormatUtils.formatMacString(fromMote),
                    FormatUtils.formatMacString(toMote)
                )
            ]
            for (k,v) in dld.getPathInfo(self.netname,fromMote,toMote).items():
                output += ['- {0}: {1}'.format(k,v)]
        output  = '\n'.join(output)
        f = open('poipoi_pathinfo.txt','w')
        f.write(output)
        f.close()
        print 'pathInfo dumped'
    '''
    
    #======================== helpers =========================================
