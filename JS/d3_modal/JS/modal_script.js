/*
Source:
    https://bl.ocks.org/lsbardel/964b454dd40bc32082a0753e9106a707
*/
(function () {

    var modal = {
        model: {
            modalTitle: "d3-view modal",
            modalBody: 'First name: <input type="text" id="idFirstName" name="FirstName" value="Mickey"><br>',
            showModal: false,
            $showModal () {
                this.showModal = true;
            },
            $hideModal () {
                document.getElementById("sel_btn").innerText = "Close";
                this.showModal = false;
            },
            $hideModalOK () {
                document.getElementById("sel_btn").innerText = "OK";
                var btn = document.getElementById("idFirstName");
                var txt;
                try {
                    txt = btn.value;
                }
                catch (err) {
                    txt = err.message;
                }
                alert (txt);
                this.showModal = false;
            }
        },
        directive: {
            refresh (model, show) {
                if (!this.passes) return;
                var sel = this.sel,
                    modal = sel.classed('modal');
                if (show) {
                    sel.style('display', 'block').classed('show', true);
                    if (modal) {
                        var height = sel.style('height');
                        sel.style('top', '-' + height);
                        this.transition(sel).ease(d3.easeExpOut).style('top', '0px');
                    }
                }
                else {
                    var op = sel.style('opacity'),
                        t = this.transition(sel);
                    sel.classed('show', false);
                    if (modal) {
                        var height = sel.style('height');
                        t.style('top', '-' + height).on('end', function () {
                            sel.style('display', 'none');
                        });
                    } else
                        t.style('opacity', 0);
                    t.on('end', function () {
                        sel.style('display', 'none').style('opacity', op);
                    });
                }
            }
        },
        render: function () {
            return this.renderFromUrl('modal_msg.html');
        }
    };

    var vm = d3.view({
        model: {
            $modal() {
                var modal = vm.select('.modal');
                if (!modal.size())
                    vm.select('body').append('modal').mount(null, v => v.model.$showModal());
                else
                    modal.model().$showModal();
            }
        },
        components: {
            modal: modal
        },
        directives: {
            modal: modal.directive
        }
    });
    vm.mount('body');
}());
