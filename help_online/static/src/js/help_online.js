odoo.define("oca.HelpOnline", function (require) {
    "use strict";

    const core = require('web.core');
    const ajax = require('web.ajax');
    const Dialog = require('web.Dialog');
    const QWeb = core.qweb;
    const _t = core._t;

    const { Component, useState, mount } = owl;
    const { xml } = owl.tags;

    class HelpOnline extends Component {
        static template = 'help_online.Button';

        async willStart() {
            var self = this;
            return ajax.jsonRpc("/help_online/build_url", 'call', {
                model: this.env.view.model,
                view_type: this.env.view.type,
            }).then(function(result) {
                self.url_info = result;
            });
        }
        mounted() {
            super.mounted(...arguments);
            var self = this;
            var $el = $(self.el);
            if (self.url_info.exists === false) {
                $el.on("click", function (event) {
                    var evt = event;
                    evt.preventDefault();
                    Dialog.confirm(
                        self,
                        _t("Page does not exist. Do you want to create?"),
                        {
                            confirm_callback: function () {
                                var form = $("<form></form>");
                                form.attr({
                                    id: "formform",
                                    // The location given in the link itself
                                    action: evt.target.href,
                                    method: "POST",
                                    // Open in new window/tab
                                    target: evt.target.target,
                                });
                                var csrf = $('<input/>');
                                csrf.attr({
                                    type: 'hidden',
                                    name: 'csrf_token',
                                    value: core.csrf_token,
                                })
                                form.append(csrf);
                                $("body").append(form);
                                $("#formform").submit();
                                $("#formform").remove();
                                return false;
                            },
                        }
                    );
                });
            }
        }

    }

    const ControlPanel = require("web.ControlPanel");

    ControlPanel.patch("help_online.ControlPanelHelpOnline", (T) => {
        class ControlPanelPatchRHelpOnline extends T {}
        ControlPanelPatchRHelpOnline.components.HelpOnline = HelpOnline;
        return ControlPanelPatchRHelpOnline;
    });

});
