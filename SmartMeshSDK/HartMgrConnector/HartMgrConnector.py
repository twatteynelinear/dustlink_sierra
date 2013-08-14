'''
This module was generated automatically. Do not edit directly.
'''

import collections
import ApiException
from   HartMgrConnectorInternal import HartMgrConnectorInternal

class HartMgrConnector(HartMgrConnectorInternal):
    '''
    \ingroup ApiConnector
    \brief Public class for the HART Manager connector using the XML API.
    '''

    #======================== commands ========================================

    ##
    # The named tuple returned by the dn_getSystem() function.
    # 
    # - <tt>systemName</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>location</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>swRev</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>hwModel</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>hwRev</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>serialNumber</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>time</tt>: 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>startTime</tt>: 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>cliTimeout</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>controllerSwRev</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getSystem = collections.namedtuple("Tuple_dn_getSystem", ['systemName', 'location', 'swRev', 'hwModel', 'hwRev', 'serialNumber', 'time', 'startTime', 'cliTimeout', 'controllerSwRev'])

    ##
    # Retrieves system-level information
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getSystem named tuple.
    # 
    def dn_getSystem(self, ) :
        res = HartMgrConnectorInternal.send(self, ['getSystem'], {})
        return HartMgrConnector.Tuple_dn_getSystem(**res)

    ##
    # The named tuple returned by the dn_getNetwork() function.
    # 
    # - <tt>netName</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>networkId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>maxMotes</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>numMotes</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>optimizationEnable</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>accessPointPA</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>ccaEnabled</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>requestedBasePkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>minServicesPkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>minPipePkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>bandwidthProfile</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>manualUSFrameSize</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>manualDSFrameSize</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>manualAdvFrameSize</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>netQueueSize</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>userQueueSize</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>locationMode</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getNetwork = collections.namedtuple("Tuple_dn_getNetwork", ['netName', 'networkId', 'maxMotes', 'numMotes', 'optimizationEnable', 'accessPointPA', 'ccaEnabled', 'requestedBasePkPeriod', 'minServicesPkPeriod', 'minPipePkPeriod', 'bandwidthProfile', 'manualUSFrameSize', 'manualDSFrameSize', 'manualAdvFrameSize', 'netQueueSize', 'userQueueSize', 'locationMode'])

    ##
    # Retrieves network configuration parameters
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getNetwork named tuple.
    # 
    def dn_getNetwork(self, ) :
        res = HartMgrConnectorInternal.send(self, ['getNetwork'], {})
        return HartMgrConnector.Tuple_dn_getNetwork(**res)

    ##
    # The named tuple returned by the dn_getNetworkStatistics() function.
    # 
    # - <tt>index</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>startTime</tt>: 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>netLatency</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>netReliability</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>netPathStability</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>lostUpstreamPackets</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getNetworkStatistics = collections.namedtuple("Tuple_dn_getNetworkStatistics", ['index', 'startTime', 'netLatency', 'netReliability', 'netPathStability', 'lostUpstreamPackets'])

    ##
    # Get the Network Statistics
    # 
    # \param period 32-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - current: current
    #      - lifetime: lifetime
    #      - short: short
    #      - long: long
    # \param index 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getNetworkStatistics named tuple.
    # 
    def dn_getNetworkStatistics(self, period, index) :
        res = HartMgrConnectorInternal.send(self, ['getNetworkStatistics'], {"period" : period, "index" : index})
        return HartMgrConnector.Tuple_dn_getNetworkStatistics(**res)

    ##
    # The named tuple returned by the dn_getMote() function.
    # 
    # - <tt>moteId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>macAddr</tt>: 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>name</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>state</tt>: 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - Idle: idle
    #      - Lost: lost
    #      - Joining: joining
    #      - Operational: operational
    # - <tt>numJoins</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>joinTime</tt>: 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>reason</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>isAccessPoint</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>powerSource</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>dischargeCurrent</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>dischargeTime</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>recoveryTime</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>enableRouting</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>productName</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>hwModel</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>hwRev</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>swRev</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>voltage</tt>: 8-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>numNeighbors</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>needNeighbor</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>goodNeighbors</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>allocatedPkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>allocatedPipePkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>pipeStatus</tt>: 4-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - on: on
    #      - off: off
    # - <tt>advertisingStatus</tt>: 4-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - on: on
    #      - off: off
    # - <tt>locationTag</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getMote = collections.namedtuple("Tuple_dn_getMote", ['moteId', 'macAddr', 'name', 'state', 'numJoins', 'joinTime', 'reason', 'isAccessPoint', 'powerSource', 'dischargeCurrent', 'dischargeTime', 'recoveryTime', 'enableRouting', 'productName', 'hwModel', 'hwRev', 'swRev', 'voltage', 'numNeighbors', 'needNeighbor', 'goodNeighbors', 'allocatedPkPeriod', 'allocatedPipePkPeriod', 'pipeStatus', 'advertisingStatus', 'locationTag'])

    ##
    # 
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getMote named tuple.
    # 
    def dn_getMote(self, macAddr) :
        res = HartMgrConnectorInternal.send(self, ['getMote'], {"macAddr" : macAddr})
        return HartMgrConnector.Tuple_dn_getMote(**res)

    ##
    # The named tuple returned by the dn_getMoteStatistics() function.
    # 
    # - <tt>index</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>startTime</tt>: 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>avgLatency</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>reliability</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>numJoins</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>numLostPackets</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getMoteStatistics = collections.namedtuple("Tuple_dn_getMoteStatistics", ['index', 'startTime', 'avgLatency', 'reliability', 'numJoins', 'numLostPackets'])

    ##
    # Get the Mote Statistics
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param period 32-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - current: current
    #      - lifetime: lifetime
    #      - short: short
    #      - long: long
    # \param index 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getMoteStatistics named tuple.
    # 
    def dn_getMoteStatistics(self, macAddr, period, index) :
        res = HartMgrConnectorInternal.send(self, ['getMoteStatistics'], {"macAddr" : macAddr, "period" : period, "index" : index})
        return HartMgrConnector.Tuple_dn_getMoteStatistics(**res)

    ##
    # The named tuple returned by the dn_getMotes() function.
    # 
    # - <tt>moteId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>macAddr</tt>: 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>name</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>state</tt>: 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - Idle: idle
    #      - Lost: lost
    #      - Joining: joining
    #      - Operational: operational
    # - <tt>numJoins</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>joinTime</tt>: 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>reason</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>isAccessPoint</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>powerSource</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>dischargeCurrent</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>dischargeTime</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>recoveryTime</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>enableRouting</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>productName</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>hwModel</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>hwRev</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>swRev</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>voltage</tt>: 8-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>numNeighbors</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>needNeighbor</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>goodNeighbors</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>allocatedPkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>allocatedPipePkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>pipeStatus</tt>: 4-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - on: on
    #      - off: off
    # - <tt>advertisingStatus</tt>: 4-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - on: on
    #      - off: off
    # - <tt>locationTag</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getMotes = collections.namedtuple("Tuple_dn_getMotes", ['moteId', 'macAddr', 'name', 'state', 'numJoins', 'joinTime', 'reason', 'isAccessPoint', 'powerSource', 'dischargeCurrent', 'dischargeTime', 'recoveryTime', 'enableRouting', 'productName', 'hwModel', 'hwRev', 'swRev', 'voltage', 'numNeighbors', 'needNeighbor', 'goodNeighbors', 'allocatedPkPeriod', 'allocatedPipePkPeriod', 'pipeStatus', 'advertisingStatus', 'locationTag'])

    ##
    # Get the list of Motes
    # 
    # 
    # 
    # \returns The response to the command, formatted as a list of #Tuple_dn_getMotes named tuple.
    # 
    def dn_getMotes(self, ) :
        res = HartMgrConnectorInternal.send(self, ['getMotes'], {})
        tupleList = []
        for r in res :
            tupleList.append(HartMgrConnector.Tuple_dn_getMotes(**r))
        return tupleList

    ##
    # The named tuple returned by the dn_getPaths() function.
    # 
    # - <tt>pathId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteAMac</tt>: 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>moteBMac</tt>: 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>numLinks</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>pathDirection</tt>: 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - all: all
    #      - upstream: upstream
    #      - downstream: downstream
    #      - used: used
    #      - unused: unused
    # - <tt>pathQuality</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getPaths = collections.namedtuple("Tuple_dn_getPaths", ['pathId', 'moteAMac', 'moteBMac', 'numLinks', 'pathDirection', 'pathQuality'])

    ##
    # Get the list of Paths to the mote's neighbors
    # 
    # \param moteMac 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a list of #Tuple_dn_getPaths named tuple.
    # 
    def dn_getPaths(self, moteMac) :
        res = HartMgrConnectorInternal.send(self, ['getPaths'], {"moteMac" : moteMac})
        tupleList = []
        for r in res :
            tupleList.append(HartMgrConnector.Tuple_dn_getPaths(**r))
        return tupleList

    ##
    # The named tuple returned by the dn_getPathStatistics() function.
    # 
    # - <tt>index</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>startTime</tt>: 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>baPwr</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>abPwr</tt>: 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>stability</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getPathStatistics = collections.namedtuple("Tuple_dn_getPathStatistics", ['index', 'startTime', 'baPwr', 'abPwr', 'stability'])

    ##
    # Get Statistics for a specific Path
    # 
    # \param pathId 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param period 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - current: current
    #      - lifetime: lifetime
    #      - short: short
    #      - long: long
    # \param index 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getPathStatistics named tuple.
    # 
    def dn_getPathStatistics(self, pathId, period, index) :
        res = HartMgrConnectorInternal.send(self, ['getPathStatistics'], {"pathId" : pathId, "period" : period, "index" : index})
        return HartMgrConnector.Tuple_dn_getPathStatistics(**res)

    ##
    # The named tuple returned by the dn_getBlacklist() function.
    # 
    # - <tt>frequency</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getBlacklist = collections.namedtuple("Tuple_dn_getBlacklist", ['frequency'])

    ##
    # 
    # 
    # 
    # 
    # \returns The response to the command, formatted as a list of #Tuple_dn_getBlacklist named tuple.
    # 
    def dn_getBlacklist(self, ) :
        res = HartMgrConnectorInternal.send(self, ['getBlacklist'], {})
        tupleList = []
        for r in res :
            tupleList.append(HartMgrConnector.Tuple_dn_getBlacklist(**r))
        return tupleList

    ##
    # The named tuple returned by the dn_getSla() function.
    # 
    # - <tt>minNetReliability</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>maxNetLatency</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>minNetPathStability</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>apRdntCoverageThreshold</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getSla = collections.namedtuple("Tuple_dn_getSla", ['minNetReliability', 'maxNetLatency', 'minNetPathStability', 'apRdntCoverageThreshold'])

    ##
    # 
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getSla named tuple.
    # 
    def dn_getSla(self, ) :
        res = HartMgrConnectorInternal.send(self, ['getSla'], {})
        return HartMgrConnector.Tuple_dn_getSla(**res)

    ##
    # The named tuple returned by the dn_getUsers() function.
    # 
    # - <tt>userName</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>privilege</tt>: 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - viewer: viewer
    #      - user: user
    #      - superuser: superuser
    # 
    Tuple_dn_getUsers = collections.namedtuple("Tuple_dn_getUsers", ['userName', 'privilege'])

    ##
    # 
    # 
    # 
    # 
    # \returns The response to the command, formatted as a list of #Tuple_dn_getUsers named tuple.
    # 
    def dn_getUsers(self, ) :
        res = HartMgrConnectorInternal.send(self, ['getUsers'], {})
        tupleList = []
        for r in res :
            tupleList.append(HartMgrConnector.Tuple_dn_getUsers(**r))
        return tupleList

    ##
    # The named tuple returned by the dn_getUser() function.
    # 
    # - <tt>userName</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>privilege</tt>: 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - viewer: viewer
    #      - user: user
    #      - superuser: superuser
    # 
    Tuple_dn_getUser = collections.namedtuple("Tuple_dn_getUser", ['userName', 'privilege'])

    ##
    # 
    # 
    # \param userName 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getUser named tuple.
    # 
    def dn_getUser(self, userName) :
        res = HartMgrConnectorInternal.send(self, ['getUser'], {"userName" : userName})
        return HartMgrConnector.Tuple_dn_getUser(**res)

    ##
    # The named tuple returned by the dn_setSystem() function.
    # 
    # - <tt>systemName</tt>: 50-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>location</tt>: 50-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>cliTimeout</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_setSystem = collections.namedtuple("Tuple_dn_setSystem", ['systemName', 'location', 'cliTimeout'])

    ##
    # 
    # 
    # \param systemName 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param location 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param cliTimeout 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setSystem named tuple.
    # 
    def dn_setSystem(self, systemName, location, cliTimeout) :
        res = HartMgrConnectorInternal.send(self, ['setSystem'], {"systemName" : systemName, "location" : location, "cliTimeout" : cliTimeout})
        return HartMgrConnector.Tuple_dn_setSystem(**res)

    ##
    # The named tuple returned by the dn_setNetwork() function.
    # 
    # - <tt>netName</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>networkId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>optimizationEnable</tt>: 6-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - true: true
    #      - false: false
    # - <tt>maxMotes</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>accessPointPA</tt>: 6-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - true: true
    #      - false: false
    # - <tt>ccaEnabled</tt>: 6-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - true: true
    #      - false: false
    # - <tt>requestedBasePkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>minServicesPkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>minPipePkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>bandwidthProfile</tt>: 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - Manual: manual
    #      - P1: p1
    #      - P2: p2
    # - <tt>manualUSFrameSize</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>manualDSFrameSize</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>manualAdvFrameSize</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>locationMode</tt>: 8-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - on: on
    #      - off: off
    # 
    Tuple_dn_setNetwork = collections.namedtuple("Tuple_dn_setNetwork", ['netName', 'networkId', 'optimizationEnable', 'maxMotes', 'accessPointPA', 'ccaEnabled', 'requestedBasePkPeriod', 'minServicesPkPeriod', 'minPipePkPeriod', 'bandwidthProfile', 'manualUSFrameSize', 'manualDSFrameSize', 'manualAdvFrameSize', 'locationMode'])

    ##
    # 
    # 
    # \param netName 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param networkId 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param optimizationEnable 6-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - true: true
    #      - false: false
    # \param maxMotes 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param accessPointPA 6-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - true: true
    #      - false: false
    # \param ccaEnabled 6-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - true: true
    #      - false: false
    # \param requestedBasePkPeriod 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param minServicesPkPeriod 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param minPipePkPeriod 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param bandwidthProfile 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - Manual: manual
    #      - P1: p1
    #      - P2: p2
    # \param manualUSFrameSize 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param manualDSFrameSize 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param manualAdvFrameSize 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param locationMode 8-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - on: on
    #      - off: off
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setNetwork named tuple.
    # 
    def dn_setNetwork(self, netName, networkId, optimizationEnable, maxMotes, accessPointPA, ccaEnabled, requestedBasePkPeriod, minServicesPkPeriod, minPipePkPeriod, bandwidthProfile, manualUSFrameSize, manualDSFrameSize, manualAdvFrameSize, locationMode) :
        res = HartMgrConnectorInternal.send(self, ['setNetwork'], {"netName" : netName, "networkId" : networkId, "optimizationEnable" : optimizationEnable, "maxMotes" : maxMotes, "accessPointPA" : accessPointPA, "ccaEnabled" : ccaEnabled, "requestedBasePkPeriod" : requestedBasePkPeriod, "minServicesPkPeriod" : minServicesPkPeriod, "minPipePkPeriod" : minPipePkPeriod, "bandwidthProfile" : bandwidthProfile, "manualUSFrameSize" : manualUSFrameSize, "manualDSFrameSize" : manualDSFrameSize, "manualAdvFrameSize" : manualAdvFrameSize, "locationMode" : locationMode})
        return HartMgrConnector.Tuple_dn_setNetwork(**res)

    ##
    # The named tuple returned by the dn_setMote() function.
    # 
    # - <tt>moteId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>macAddr</tt>: 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>name</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>state</tt>: 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - Idle: idle
    #      - Lost: lost
    #      - Joining: joining
    #      - Operational: operational
    # - <tt>numJoins</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>joinTime</tt>: 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>reason</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>isAccessPoint</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>powerSource</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>dischargeCurrent</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>dischargeTime</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>recoveryTime</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>enableRouting</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>productName</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>hwModel</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>hwRev</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>swRev</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>voltage</tt>: 8-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>numNeighbors</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>needNeighbor</tt>: 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>goodNeighbors</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>allocatedPkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>allocatedPipePkPeriod</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>pipeStatus</tt>: 4-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - on: on
    #      - off: off
    # - <tt>advertisingStatus</tt>: 4-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - on: on
    #      - off: off
    # - <tt>locationTag</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_setMote = collections.namedtuple("Tuple_dn_setMote", ['moteId', 'macAddr', 'name', 'state', 'numJoins', 'joinTime', 'reason', 'isAccessPoint', 'powerSource', 'dischargeCurrent', 'dischargeTime', 'recoveryTime', 'enableRouting', 'productName', 'hwModel', 'hwRev', 'swRev', 'voltage', 'numNeighbors', 'needNeighbor', 'goodNeighbors', 'allocatedPkPeriod', 'allocatedPipePkPeriod', 'pipeStatus', 'advertisingStatus', 'locationTag'])

    ##
    # 
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param name 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param enableRouting 6-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - true: true
    #      - false: false
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setMote named tuple.
    # 
    def dn_setMote(self, macAddr, name, enableRouting) :
        res = HartMgrConnectorInternal.send(self, ['setMote'], {"macAddr" : macAddr, "name" : name, "enableRouting" : enableRouting})
        return HartMgrConnector.Tuple_dn_setMote(**res)

    ##
    # The named tuple returned by the dn_setSla() function.
    # 
    # - <tt>minNetReliability</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>maxNetLatency</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>minNetPathStability</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>apRdntCoverageThreshold</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_setSla = collections.namedtuple("Tuple_dn_setSla", ['minNetReliability', 'maxNetLatency', 'minNetPathStability', 'apRdntCoverageThreshold'])

    ##
    # 
    # 
    # \param minNetReliability 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # \param maxNetLatency 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param minNetPathStability 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # \param apRdntCoverageThreshold 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setSla named tuple.
    # 
    def dn_setSla(self, minNetReliability, maxNetLatency, minNetPathStability, apRdntCoverageThreshold) :
        res = HartMgrConnectorInternal.send(self, ['setSla'], {"minNetReliability" : minNetReliability, "maxNetLatency" : maxNetLatency, "minNetPathStability" : minNetPathStability, "apRdntCoverageThreshold" : apRdntCoverageThreshold})
        return HartMgrConnector.Tuple_dn_setSla(**res)

    ##
    # The named tuple returned by the dn_setSecurity() function.
    # 
    # - <tt>securityMode</tt>: 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - acceptACL: acceptacl
    #      - acceptCommonJoinKey: acceptcommonjoinkey
    # - <tt>commonJoinKey</tt>: 33-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>acceptHARTDevicesOnly</tt>: 6-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - true: true
    #      - false: false
    # 
    Tuple_dn_setSecurity = collections.namedtuple("Tuple_dn_setSecurity", ['securityMode', 'commonJoinKey', 'acceptHARTDevicesOnly'])

    ##
    # 
    # 
    # \param securityMode 25-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - acceptACL: acceptacl
    #      - acceptCommonJoinKey: acceptcommonjoinkey
    # \param commonJoinKey 33-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param acceptHARTDevicesOnly 6-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - true: true
    #      - false: false
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setSecurity named tuple.
    # 
    def dn_setSecurity(self, securityMode, commonJoinKey, acceptHARTDevicesOnly) :
        res = HartMgrConnectorInternal.send(self, ['setSecurity'], {"securityMode" : securityMode, "commonJoinKey" : commonJoinKey, "acceptHARTDevicesOnly" : acceptHARTDevicesOnly})
        return HartMgrConnector.Tuple_dn_setSecurity(**res)

    ##
    # The named tuple returned by the dn_setUser() function.
    # 
    # - <tt>userName</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>password</tt>: 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>privilege</tt>: 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - viewer: viewer
    #      - user: user
    #      - superuser: superuser
    # 
    Tuple_dn_setUser = collections.namedtuple("Tuple_dn_setUser", ['userName', 'password', 'privilege'])

    ##
    # 
    # 
    # \param userName 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param password 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param privilege 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - viewer: viewer
    #      - user: user
    #      - superuser: superuser
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setUser named tuple.
    # 
    def dn_setUser(self, userName, password, privilege) :
        res = HartMgrConnectorInternal.send(self, ['setUser'], {"userName" : userName, "password" : password, "privilege" : privilege})
        return HartMgrConnector.Tuple_dn_setUser(**res)

    ##
    # The named tuple returned by the dn_setAcl() function.
    # 
    # - <tt>macAddr</tt>: 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>joinKey</tt>: 33-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_setAcl = collections.namedtuple("Tuple_dn_setAcl", ['macAddr', 'joinKey'])

    ##
    # 
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param joinKey 33-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setAcl named tuple.
    # 
    def dn_setAcl(self, macAddr, joinKey) :
        res = HartMgrConnectorInternal.send(self, ['setAcl'], {"macAddr" : macAddr, "joinKey" : joinKey})
        return HartMgrConnector.Tuple_dn_setAcl(**res)

    ##
    # The named tuple returned by the dn_setBlackList() function.
    # 
    # - <tt>frequency</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_setBlackList = collections.namedtuple("Tuple_dn_setBlackList", ['frequency'])

    ##
    # 
    # 
    # \param frequency 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setBlackList named tuple.
    # 
    def dn_setBlackList(self, frequency) :
        res = HartMgrConnectorInternal.send(self, ['setBlackList'], {"frequency" : frequency})
        return HartMgrConnector.Tuple_dn_setBlackList(**res)

    ##
    # 
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command.
    # 
    def dn_deleteAcl(self, macAddr) :
        res = HartMgrConnectorInternal.send(self, ['deleteAcl'], {"macAddr" : macAddr})
        return res

    ##
    # 
    # 
    # \param userName 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command.
    # 
    def dn_deleteUser(self, userName) :
        res = HartMgrConnectorInternal.send(self, ['deleteUser'], {"userName" : userName})
        return res

    ##
    # 
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command.
    # 
    def dn_deleteMote(self, macAddr) :
        res = HartMgrConnectorInternal.send(self, ['deleteMote'], {"macAddr" : macAddr})
        return res

    ##
    # The named tuple returned by the dn_sendRequest() function.
    # 
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_sendRequest = collections.namedtuple("Tuple_dn_sendRequest", ['callbackId'])

    ##
    # 
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param domain 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - maintenance: maintenance
    # \param priority 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - low: low
    #      - high: high
    # \param reliable 0-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # \param data 128-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_sendRequest named tuple.
    # 
    def dn_sendRequest(self, macAddr, domain, priority, reliable, data) :
        res = HartMgrConnectorInternal.send(self, ['sendRequest'], {"macAddr" : macAddr, "domain" : domain, "priority" : priority, "reliable" : reliable, "data" : data})
        return HartMgrConnector.Tuple_dn_sendRequest(**res)

    ##
    # The named tuple returned by the dn_sendResponse() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_sendResponse = collections.namedtuple("Tuple_dn_sendResponse", ['result'])

    ##
    # 
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param domain 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - maintenance: maintenance
    # \param priority 16-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - low: low
    #      - high: high
    # \param reliable 0-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    # \param callbackId 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # \param data 128-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_sendResponse named tuple.
    # 
    def dn_sendResponse(self, macAddr, domain, priority, reliable, callbackId, data) :
        res = HartMgrConnectorInternal.send(self, ['sendResponse'], {"macAddr" : macAddr, "domain" : domain, "priority" : priority, "reliable" : reliable, "callbackId" : callbackId, "data" : data})
        return HartMgrConnector.Tuple_dn_sendResponse(**res)

    ##
    # The named tuple returned by the dn_exchangeNetworkKey() function.
    # 
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_exchangeNetworkKey = collections.namedtuple("Tuple_dn_exchangeNetworkKey", ['callbackId'])

    ##
    # Exchange network key
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_exchangeNetworkKey named tuple.
    # 
    def dn_exchangeNetworkKey(self, ) :
        res = HartMgrConnectorInternal.send(self, ['exchangeNetworkKey'], {})
        return HartMgrConnector.Tuple_dn_exchangeNetworkKey(**res)

    ##
    # The named tuple returned by the dn_exchangeJoinKey() function.
    # 
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_exchangeJoinKey = collections.namedtuple("Tuple_dn_exchangeJoinKey", ['callbackId'])

    ##
    # Exchange common join key
    # 
    # \param newKey 33-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_exchangeJoinKey named tuple.
    # 
    def dn_exchangeJoinKey(self, newKey) :
        res = HartMgrConnectorInternal.send(self, ['exchangeJoinKey'], {"newKey" : newKey})
        return HartMgrConnector.Tuple_dn_exchangeJoinKey(**res)

    ##
    # The named tuple returned by the dn_exchangeMoteJoinKey() function.
    # 
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_exchangeMoteJoinKey = collections.namedtuple("Tuple_dn_exchangeMoteJoinKey", ['callbackId'])

    ##
    # Exchange mote join key
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param newKey 33-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_exchangeMoteJoinKey named tuple.
    # 
    def dn_exchangeMoteJoinKey(self, macAddr, newKey) :
        res = HartMgrConnectorInternal.send(self, ['exchangeMoteJoinKey'], {"macAddr" : macAddr, "newKey" : newKey})
        return HartMgrConnector.Tuple_dn_exchangeMoteJoinKey(**res)

    ##
    # The named tuple returned by the dn_exchangeNetworkId() function.
    # 
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_exchangeNetworkId = collections.namedtuple("Tuple_dn_exchangeNetworkId", ['callbackId'])

    ##
    # Exchange network ID
    # 
    # \param newId 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_exchangeNetworkId named tuple.
    # 
    def dn_exchangeNetworkId(self, newId) :
        res = HartMgrConnectorInternal.send(self, ['exchangeNetworkId'], {"newId" : newId})
        return HartMgrConnector.Tuple_dn_exchangeNetworkId(**res)

    ##
    # The named tuple returned by the dn_exchangeMoteNetworkId() function.
    # 
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_exchangeMoteNetworkId = collections.namedtuple("Tuple_dn_exchangeMoteNetworkId", ['callbackId'])

    ##
    # Exchange network ID for mote
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param newId 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_exchangeMoteNetworkId named tuple.
    # 
    def dn_exchangeMoteNetworkId(self, macAddr, newId) :
        res = HartMgrConnectorInternal.send(self, ['exchangeMoteNetworkId'], {"macAddr" : macAddr, "newId" : newId})
        return HartMgrConnector.Tuple_dn_exchangeMoteNetworkId(**res)

    ##
    # The named tuple returned by the dn_exchangeSessionKey() function.
    # 
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_exchangeSessionKey = collections.namedtuple("Tuple_dn_exchangeSessionKey", ['callbackId'])

    ##
    # Exchange mote session key
    # 
    # \param macAddrA 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param macAddrB 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_exchangeSessionKey named tuple.
    # 
    def dn_exchangeSessionKey(self, macAddrA, macAddrB) :
        res = HartMgrConnectorInternal.send(self, ['exchangeSessionKey'], {"macAddrA" : macAddrA, "macAddrB" : macAddrB})
        return HartMgrConnector.Tuple_dn_exchangeSessionKey(**res)

    ##
    # The named tuple returned by the dn_activateFastPipe() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_activateFastPipe = collections.namedtuple("Tuple_dn_activateFastPipe", ['result'])

    ##
    # Activate the fast network pipe to the specified mote.
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param pipeDirection 25-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - UniUp: upstream
    #      - UniDown: downstream
    #      - Bi: bidirectional
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_activateFastPipe named tuple.
    # 
    def dn_activateFastPipe(self, macAddr, pipeDirection) :
        res = HartMgrConnectorInternal.send(self, ['activateFastPipe'], {"macAddr" : macAddr, "pipeDirection" : pipeDirection})
        return HartMgrConnector.Tuple_dn_activateFastPipe(**res)

    ##
    # The named tuple returned by the dn_deactivateFastPipe() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_deactivateFastPipe = collections.namedtuple("Tuple_dn_deactivateFastPipe", ['result'])

    ##
    # Deactivate the fast network pipe to the specified mote.
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_deactivateFastPipe named tuple.
    # 
    def dn_deactivateFastPipe(self, macAddr) :
        res = HartMgrConnectorInternal.send(self, ['deactivateFastPipe'], {"macAddr" : macAddr})
        return HartMgrConnector.Tuple_dn_deactivateFastPipe(**res)

    ##
    # The named tuple returned by the dn_getLatency() function.
    # 
    # - <tt>downstream</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>upstream</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getLatency = collections.namedtuple("Tuple_dn_getLatency", ['downstream', 'upstream'])

    ##
    # Get estimated latency for a mote.
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getLatency named tuple.
    # 
    def dn_getLatency(self, macAddr) :
        res = HartMgrConnectorInternal.send(self, ['getLatency'], {"macAddr" : macAddr})
        return HartMgrConnector.Tuple_dn_getLatency(**res)

    ##
    # The named tuple returned by the dn_getTime() function.
    # 
    # - <tt>utc_time</tt>: 0-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    # - <tt>asn_time</tt>: 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getTime = collections.namedtuple("Tuple_dn_getTime", ['utc_time', 'asn_time'])

    ##
    # Get the current time.
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getTime named tuple.
    # 
    def dn_getTime(self, ) :
        res = HartMgrConnectorInternal.send(self, ['getTime'], {})
        return HartMgrConnector.Tuple_dn_getTime(**res)

    ##
    # The named tuple returned by the dn_advertising() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_advertising = collections.namedtuple("Tuple_dn_advertising", ['result'])

    ##
    # Activate advertisement frame
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # \param timeout 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_advertising named tuple.
    # 
    def dn_advertising(self, macAddr, timeout) :
        res = HartMgrConnectorInternal.send(self, ['advertising'], {"macAddr" : macAddr, "timeout" : timeout})
        return HartMgrConnector.Tuple_dn_advertising(**res)

    ##
    # The named tuple returned by the dn_decommission() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_decommission = collections.namedtuple("Tuple_dn_decommission", ['result'])

    ##
    # Device decommission
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_decommission named tuple.
    # 
    def dn_decommission(self, macAddr) :
        res = HartMgrConnectorInternal.send(self, ['decommission'], {"macAddr" : macAddr})
        return HartMgrConnector.Tuple_dn_decommission(**res)

    ##
    # The named tuple returned by the dn_ping() function.
    # 
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_ping = collections.namedtuple("Tuple_dn_ping", ['callbackId'])

    ##
    # Ping the specified mote. A Net Ping Reply event notification will contain the mote's response.
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_ping named tuple.
    # 
    def dn_ping(self, macAddr) :
        res = HartMgrConnectorInternal.send(self, ['ping'], {"macAddr" : macAddr})
        return HartMgrConnector.Tuple_dn_ping(**res)

    ##
    # The named tuple returned by the dn_getLicense() function.
    # 
    # - <tt>license</tt>: 40-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_getLicense = collections.namedtuple("Tuple_dn_getLicense", ['license'])

    ##
    # Get license
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_getLicense named tuple.
    # 
    def dn_getLicense(self, ) :
        res = HartMgrConnectorInternal.send(self, ['getLicense'], {})
        return HartMgrConnector.Tuple_dn_getLicense(**res)

    ##
    # The named tuple returned by the dn_setLicense() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_setLicense = collections.namedtuple("Tuple_dn_setLicense", ['result'])

    ##
    # Set license
    # 
    # \param license 40-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_setLicense named tuple.
    # 
    def dn_setLicense(self, license) :
        res = HartMgrConnectorInternal.send(self, ['setLicense'], {"license" : license})
        return HartMgrConnector.Tuple_dn_setLicense(**res)

    ##
    # The named tuple returned by the dn_stopLocation() function.
    # 
    # - <tt>callbackId</tt>: 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_stopLocation = collections.namedtuple("Tuple_dn_stopLocation", ['callbackId'])

    ##
    # Stop location
    # 
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_stopLocation named tuple.
    # 
    def dn_stopLocation(self, macAddr) :
        res = HartMgrConnectorInternal.send(self, ['stopLocation'], {"macAddr" : macAddr})
        return HartMgrConnector.Tuple_dn_stopLocation(**res)

    ##
    # The named tuple returned by the dn_reset() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_reset = collections.namedtuple("Tuple_dn_reset", ['result'])

    ##
    # Reset
    # 
    # \param object 25-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - network: network
    #      - system: system
    #      - stat: stat
    #      - eventLog: eventLog
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_reset named tuple.
    # 
    def dn_reset(self, object) :
        res = HartMgrConnectorInternal.send(self, ['reset'], {"object" : object})
        return HartMgrConnector.Tuple_dn_reset(**res)

    ##
    # The named tuple returned by the dn_resetWithId() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_resetWithId = collections.namedtuple("Tuple_dn_resetWithId", ['result'])

    ##
    # Reset mote by ID
    # 
    # \param object 25-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - mote: mote
    # \param moteId 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_resetWithId named tuple.
    # 
    def dn_resetWithId(self, object, moteId) :
        res = HartMgrConnectorInternal.send(self, ['resetWithId'], {"object" : object, "moteId" : moteId})
        return HartMgrConnector.Tuple_dn_resetWithId(**res)

    ##
    # The named tuple returned by the dn_resetWithMac() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_resetWithMac = collections.namedtuple("Tuple_dn_resetWithMac", ['result'])

    ##
    # Reset mote by MAC address
    # 
    # \param object 25-byte field formatted as a string.<br/>
    #     This field can only take one of the following values:
    #      - mote: mote
    # \param macAddr 25-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_resetWithMac named tuple.
    # 
    def dn_resetWithMac(self, object, macAddr) :
        res = HartMgrConnectorInternal.send(self, ['resetWithMac'], {"object" : object, "macAddr" : macAddr})
        return HartMgrConnector.Tuple_dn_resetWithMac(**res)

    ##
    # The named tuple returned by the dn_cli() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_cli = collections.namedtuple("Tuple_dn_cli", ['result'])

    ##
    # Run CLI command
    # 
    # \param command 128-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_cli named tuple.
    # 
    def dn_cli(self, command) :
        res = HartMgrConnectorInternal.send(self, ['cli'], {"command" : command})
        return HartMgrConnector.Tuple_dn_cli(**res)

    ##
    # The named tuple returned by the dn_subscribe() function.
    # 
    # - <tt>notif_token</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_subscribe = collections.namedtuple("Tuple_dn_subscribe", ['notif_token'])

    ##
    # Subscribe to notifications. This function creates or updates the subscribed notifications to match 'filter'. The filter is a space-separated list of notification types. Valid types include 'data', 'events', 'alarms', 'log'.
    # 
    # \param filter 128-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_subscribe named tuple.
    # 
    def dn_subscribe(self, filter) :
        res = HartMgrConnectorInternal.send(self, ['subscribe'], {"filter" : filter})
        return HartMgrConnector.Tuple_dn_subscribe(**res)

    ##
    # The named tuple returned by the dn_unsubscribe() function.
    # 
    # - <tt>result</tt>: 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    # 
    Tuple_dn_unsubscribe = collections.namedtuple("Tuple_dn_unsubscribe", ['result'])

    ##
    # Unsubscribe from notifications. This function clears any existing notification subscription and stops the notification thread. 
    # 
    # 
    # 
    # \returns The response to the command, formatted as a #Tuple_dn_unsubscribe named tuple.
    # 
    def dn_unsubscribe(self, ) :
        res = HartMgrConnectorInternal.send(self, ['unsubscribe'], {})
        return HartMgrConnector.Tuple_dn_unsubscribe(**res)

    #======================== notifications ===================================
    
    ##
    # Dictionary of all notification tuples.
    #
    notifTupleTable = {}
    
    ##
    # \brief USERCONNECT notification.
    # 
    # 
    #
    # Formatted as a Tuple_UserConnect named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>channel</tt> 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>ipAddr</tt> 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>userName</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    USERCONNECT = "UserConnect"
    notifTupleTable[USERCONNECT] = Tuple_UserConnect = collections.namedtuple("Tuple_UserConnect", ['timeStamp', 'eventId', 'channel', 'ipAddr', 'userName'])

    ##
    # \brief USERDISCONNECT notification.
    # 
    # 
    #
    # Formatted as a Tuple_UserDisconnect named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>channel</tt> 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>ipAddr</tt> 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>userName</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    USERDISCONNECT = "UserDisconnect"
    notifTupleTable[USERDISCONNECT] = Tuple_UserDisconnect = collections.namedtuple("Tuple_UserDisconnect", ['timeStamp', 'eventId', 'channel', 'ipAddr', 'userName'])

    ##
    # \brief MANUALMOTERESET notification.
    # 
    # 
    #
    # Formatted as a Tuple_ManualMoteReset named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>userName</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    MANUALMOTERESET = "ManualMoteReset"
    notifTupleTable[MANUALMOTERESET] = Tuple_ManualMoteReset = collections.namedtuple("Tuple_ManualMoteReset", ['timeStamp', 'eventId', 'userName', 'moteId', 'macAddr'])

    ##
    # \brief BOOTUP notification.
    # 
    # 
    #
    # Formatted as a Tuple_BootUp named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    BOOTUP = "BootUp"
    notifTupleTable[BOOTUP] = Tuple_BootUp = collections.namedtuple("Tuple_BootUp", ['timeStamp', 'eventId'])

    ##
    # \brief NETWORKRESET notification.
    # 
    # 
    #
    # Formatted as a Tuple_NetworkReset named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    NETWORKRESET = "NetworkReset"
    notifTupleTable[NETWORKRESET] = Tuple_NetworkReset = collections.namedtuple("Tuple_NetworkReset", ['timeStamp', 'eventId'])

    ##
    # \brief COMMANDFINISHED notification.
    # 
    # 
    #
    # Formatted as a Tuple_CommandFinished named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>callbackId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>result</tt> 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    COMMANDFINISHED = "CommandFinished"
    notifTupleTable[COMMANDFINISHED] = Tuple_CommandFinished = collections.namedtuple("Tuple_CommandFinished", ['timeStamp', 'eventId', 'callbackId', 'result'])

    ##
    # \brief PACKETSENT notification.
    # 
    # 
    #
    # Formatted as a Tuple_PacketSent named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>callbackId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    PACKETSENT = "PacketSent"
    notifTupleTable[PACKETSENT] = Tuple_PacketSent = collections.namedtuple("Tuple_PacketSent", ['timeStamp', 'eventId', 'callbackId'])

    ##
    # \brief MOTEJOIN notification.
    # 
    # 
    #
    # Formatted as a Tuple_MoteJoin named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>reason</tt> 64-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>userData</tt> 64-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    MOTEJOIN = "MoteJoin"
    notifTupleTable[MOTEJOIN] = Tuple_MoteJoin = collections.namedtuple("Tuple_MoteJoin", ['timeStamp', 'eventId', 'moteId', 'macAddr', 'reason', 'userData'])

    ##
    # \brief MOTELIVE notification.
    # 
    # 
    #
    # Formatted as a Tuple_MoteLive named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>reason</tt> 64-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    MOTELIVE = "MoteLive"
    notifTupleTable[MOTELIVE] = Tuple_MoteLive = collections.namedtuple("Tuple_MoteLive", ['timeStamp', 'eventId', 'moteId', 'macAddr', 'reason'])

    ##
    # \brief MOTEUNKNOWN notification.
    # 
    # 
    #
    # Formatted as a Tuple_MoteUnknown named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>reason</tt> 64-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    MOTEUNKNOWN = "MoteUnknown"
    notifTupleTable[MOTEUNKNOWN] = Tuple_MoteUnknown = collections.namedtuple("Tuple_MoteUnknown", ['timeStamp', 'eventId', 'moteId', 'macAddr', 'reason'])

    ##
    # \brief MOTEDISCONNECT notification.
    # 
    # 
    #
    # Formatted as a Tuple_MoteDisconnect named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>reason</tt> 64-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    MOTEDISCONNECT = "MoteDisconnect"
    notifTupleTable[MOTEDISCONNECT] = Tuple_MoteDisconnect = collections.namedtuple("Tuple_MoteDisconnect", ['timeStamp', 'eventId', 'moteId', 'macAddr', 'reason'])

    ##
    # \brief MOTEJOINFAILURE notification.
    # 
    # 
    #
    # Formatted as a Tuple_MoteJoinFailure named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>reason</tt> 64-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    MOTEJOINFAILURE = "MoteJoinFailure"
    notifTupleTable[MOTEJOINFAILURE] = Tuple_MoteJoinFailure = collections.namedtuple("Tuple_MoteJoinFailure", ['timeStamp', 'eventId', 'macAddr', 'reason'])

    ##
    # \brief INVALIDMIC notification.
    # 
    # 
    #
    # Formatted as a Tuple_InvalidMIC named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    INVALIDMIC = "InvalidMIC"
    notifTupleTable[INVALIDMIC] = Tuple_InvalidMIC = collections.namedtuple("Tuple_InvalidMIC", ['timeStamp', 'eventId', 'macAddr'])

    ##
    # \brief PATHCREATE notification.
    # 
    # 
    #
    # Formatted as a Tuple_PathCreate named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>pathId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteAMac</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteBMac</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    PATHCREATE = "PathCreate"
    notifTupleTable[PATHCREATE] = Tuple_PathCreate = collections.namedtuple("Tuple_PathCreate", ['timeStamp', 'eventId', 'pathId', 'moteAMac', 'moteBMac'])

    ##
    # \brief PATHDELETE notification.
    # 
    # 
    #
    # Formatted as a Tuple_PathDelete named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>pathId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteAMac</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteBMac</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    PATHDELETE = "PathDelete"
    notifTupleTable[PATHDELETE] = Tuple_PathDelete = collections.namedtuple("Tuple_PathDelete", ['timeStamp', 'eventId', 'pathId', 'moteAMac', 'moteBMac'])

    ##
    # \brief PATHACTIVATE notification.
    # 
    # 
    #
    # Formatted as a Tuple_PathActivate named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>pathId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteAMac</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteBMac</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    PATHACTIVATE = "PathActivate"
    notifTupleTable[PATHACTIVATE] = Tuple_PathActivate = collections.namedtuple("Tuple_PathActivate", ['timeStamp', 'eventId', 'pathId', 'moteAMac', 'moteBMac'])

    ##
    # \brief PATHDEACTIVATE notification.
    # 
    # 
    #
    # Formatted as a Tuple_PathDeactivate named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>pathId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteAMac</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>moteBMac</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    PATHDEACTIVATE = "PathDeactivate"
    notifTupleTable[PATHDEACTIVATE] = Tuple_PathDeactivate = collections.namedtuple("Tuple_PathDeactivate", ['timeStamp', 'eventId', 'pathId', 'moteAMac', 'moteBMac'])

    ##
    # \brief PIPEON notification.
    # 
    # 
    #
    # Formatted as a Tuple_PipeOn named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    PIPEON = "PipeOn"
    notifTupleTable[PIPEON] = Tuple_PipeOn = collections.namedtuple("Tuple_PipeOn", ['timeStamp', 'eventId', 'macAddr'])

    ##
    # \brief PIPEOFF notification.
    # 
    # 
    #
    # Formatted as a Tuple_PipeOff named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    PIPEOFF = "PipeOff"
    notifTupleTable[PIPEOFF] = Tuple_PipeOff = collections.namedtuple("Tuple_PipeOff", ['timeStamp', 'eventId', 'macAddr'])

    ##
    # \brief PINGREPLY notification.
    # 
    # 
    #
    # Formatted as a Tuple_PingReply named tuple. It contains the following fields:
    #   - <tt>timeStamp</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>eventId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>callbackId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>latency</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>temperature</tt> 8-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>voltage</tt> 8-byte field formatted as a float.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>hopCount</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    PINGREPLY = "PingReply"
    notifTupleTable[PINGREPLY] = Tuple_PingReply = collections.namedtuple("Tuple_PingReply", ['timeStamp', 'eventId', 'macAddr', 'callbackId', 'latency', 'temperature', 'voltage', 'hopCount'])

    ##
    # \brief DATA notification.
    # 
    # 
    #
    # Formatted as a Tuple_data named tuple. It contains the following fields:
    #   - <tt>moteId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>macAddr</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>time</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>payload</tt> 256-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>payloadType</tt> 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>isReliable</tt> 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>isRequest</tt> 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>isBroadcast</tt> 1-byte field formatted as a bool.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>callbackId</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>counter</tt> 4-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.    
    # 
    DATA = "data"
    notifTupleTable[DATA] = Tuple_data = collections.namedtuple("Tuple_data", ['moteId', 'macAddr', 'time', 'payload', 'payloadType', 'isReliable', 'isRequest', 'isBroadcast', 'callbackId', 'counter'])

    ##
    # \brief LOCATION notification.
    # 
    # 
    #
    # Formatted as a Tuple_Location named tuple. It contains the following fields:
    #   - <tt>ver</tt> 1-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>asn</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>src</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>dest</tt> 32-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>payload</tt> 256-byte field formatted as a hex.<br/>
    #     There is no restriction on the value of this field.    
    # 
    LOCATION = "Location"
    notifTupleTable[LOCATION] = Tuple_Location = collections.namedtuple("Tuple_Location", ['ver', 'asn', 'src', 'dest', 'payload'])

    ##
    # \brief CLI notification.
    # 
    # 
    #
    # Formatted as a Tuple_cli named tuple. It contains the following fields:
    #   - <tt>time</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>message</tt> 128-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    CLI = "cli"
    notifTupleTable[CLI] = Tuple_cli = collections.namedtuple("Tuple_cli", ['time', 'message'])

    ##
    # \brief LOG notification.
    # 
    # 
    #
    # Formatted as a Tuple_log named tuple. It contains the following fields:
    #   - <tt>time</tt> 8-byte field formatted as a int.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>severity</tt> 16-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.
    #   - <tt>message</tt> 128-byte field formatted as a string.<br/>
    #     There is no restriction on the value of this field.    
    # 
    LOG = "log"
    notifTupleTable[LOG] = Tuple_log = collections.namedtuple("Tuple_log", ['time', 'severity', 'message'])

    ##
    # \brief Get a notification from the notification queue, and returns
    #        it properly formatted.
    #
    # \exception NotificationError if unknown notification.
    # 
    def getNotification(self, timeoutSec=-1) :
        temp = self.getNotificationInternal(timeoutSec)
        if not temp:
            return temp
        (ids, param) = temp
        try :
            if  HartMgrConnector.notifTupleTable[ids[-1]] :
                return (ids[-1], HartMgrConnector.notifTupleTable[ids[-1]](**param))
            else :
                return (ids[-1], None)
        except KeyError :
            raise ApiException.NotificationError(ids, param)