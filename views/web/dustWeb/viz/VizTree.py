import logging
class NullHandler(logging.Handler):
    def emit(self, record):
        pass
log = logging.getLogger('VizTree')
log.setLevel(logging.ERROR)
log.addHandler(NullHandler())

import VizD3

class VizTree(VizD3.VizD3):
    
    #======================== header ==========================================
    
    templateHeader = '''
<style type="text/css">

    .node circle {{
        cursor: pointer;
        fill: #fff;
        stroke: steelblue;
        stroke-width: 1.5px;
    }}

    .node text {{
        font-size: 11px;
    }}

    path.link {{
        fill: none;
        stroke: #ccc;
        stroke-width: 1.5px;
    }}

</style>
'''
    
    #======================== body ============================================
    
    templateBody = '''
<div id='chart_div_{VIZID}'></div>
<script type="text/javascript">

    var m = [20, 120, 20, 120],
        w = {WIDTH} - m[1] - m[3],
        h = {HEIGHT} - m[0] - m[2],
        i = 0,
        treestep = 80,
        root_{VIZID};

    var tree_{VIZID} = d3.layout.tree()
        .size([h, w]);

    var diagonal = d3.svg.diagonal()
        .projection(function(d) {{ return [d.y, d.x]; }});

    var vis_{VIZID} = d3.select("#chart_div_{VIZID}").append("svg:svg")
        .attr("width", w + m[1] + m[3])
        .attr("height", h + m[0] + m[2])
      .append("svg:g")
        .attr("transform", "translate(" + m[3] + "," + m[0] + ")");

    d3.json("/{RESOURCE}/", function(json) {{
        root_{VIZID}    = json;
        root_{VIZID}.x0 = h / 2;
        root_{VIZID}.y0 = 0;

        function toggleAll(d) {{
            if (d.children) {{
                d.children.forEach(toggleAll);
                toggle_{VIZID}(d);
            }}
        }}

        // Initialize the display to show a few nodes.
        /*
        root_{VIZID}.children.forEach(toggleAll);
        toggle_{VIZID}(root_{VIZID}.children[1]);
        toggle_{VIZID}(root_{VIZID}.children[1].children[2]);
        toggle_{VIZID}(root_{VIZID}.children[9]);
        toggle_{VIZID}(root_{VIZID}.children[9].children[0]);
        */
          
        update_{VIZID}(root_{VIZID});
    }});

    function update_{VIZID}(source) {{
        var duration = d3.event && d3.event.altKey ? 5000 : 500;

        // Compute the new tree layout.
        var nodes = tree_{VIZID}.nodes(root_{VIZID}).reverse();

        // Normalize for fixed-depth.
        nodes.forEach(function(d) {{ d.y = d.depth * treestep; }});

        // Update the nodes
        var node = vis_{VIZID}.selectAll("g.node")
            .data(nodes, function(d) {{ return d.id || (d.id = ++i); }});

        // Enter any new nodes at the parent's previous position.
        var nodeEnter = node.enter().append("svg:g")
            .attr("class", "node")
            .attr("transform", function(d) {{ return "translate(" + source.y0 + "," + source.x0 + ")"; }})
            .on("click", function(d) {{ toggle_{VIZID}(d); update_{VIZID}(d); }});

        nodeEnter.append("svg:circle")
            .attr("r", 1e-6)
            .style("fill", function(d) {{ return d._children ? "lightsteelblue" : "#fff"; }});

        nodeEnter.append("svg:text")
            .attr("x", function(d) {{ return d.children || d._children ? -10 : 10; }})
            .attr("dy", ".35em")
            .attr("text-anchor", function(d) {{ return d.children || d._children ? "end" : "start"; }})
            .text(function(d) {{ return d.name; }})
            .style("fill-opacity", 1e-6);

        // Transition nodes to their new position.
        var nodeUpdate = node.transition()
            .duration(duration)
            .attr("transform", function(d) {{ return "translate(" + d.y + "," + d.x + ")"; }});

        nodeUpdate.select("circle")
            .attr("r", 4.5)
            .style("fill", function(d) {{ return d._children ? "lightsteelblue" : "#fff"; }});

        nodeUpdate.select("text")
            .style("fill-opacity", 1);

        // Transition exiting nodes to the parent's new position.
        var nodeExit = node.exit().transition()
            .duration(duration)
            .attr("transform", function(d) {{ return "translate(" + source.y + "," + source.x + ")"; }})
            .remove();

        nodeExit.select("circle")
            .attr("r", 1e-6);

        nodeExit.select("text")
            .style("fill-opacity", 1e-6);

        // Update the links
        var link = vis_{VIZID}.selectAll("path.link")
            .data(tree_{VIZID}.links(nodes), function(d) {{ return d.target.id; }});

        // Enter any new links at the parent's previous position.
        link.enter().insert("svg:path", "g")
            .attr("class", "link")
            .attr("d", function(d) {{
                var o = {{x: source.x0, y: source.y0}};
                return diagonal({{source: o, target: o}});
            }})
          .transition()
            .duration(duration)
            .attr("d", diagonal);

        // Transition links to their new position.
        link.transition()
            .duration(duration)
            .attr("d", diagonal);

        // Transition exiting nodes to the parent's new position.
        link.exit().transition()
            .duration(duration)
            .attr("d", function(d) {{
                var o = {{x: source.x, y: source.y}};
                return diagonal({{source: o, target: o}});
            }})
            .remove();

        // Stash the old positions for transition.
        nodes.forEach(function(d) {{
            d.x0 = d.x;
            d.y0 = d.y;
        }});
    }}

    // Toggle children.
    function toggle_{VIZID}(d) {{
        if (d.children) {{
            d._children = d.children;
            d.children = null;
        }} else {{
            d.children = d._children;
            d._children = null;
        }}
    }}

</script>
'''
    