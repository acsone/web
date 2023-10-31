/** @odoo-module **/
/* global ace */

import { loadJS } from "@web/core/assets";
import { AceField } from "@web/views/fields/ace/ace_field

import { patch } from "@web/core/utils/patch";

import { onWillStart } from "@odoo/owl";

patch(AceField, "web_ace_mode_json.ace_ditor_with_mod_json", {
    setup() {
        this._super();
        onWillStart(async () => {
            const jsLibs = [
                "/web_ace_mode_json/static/lib/ace/mode-json.js",
            ];
            const proms = jsLibs.map((url) => loadJS(url));
            return Promise.all(proms);
        });
    }
});
