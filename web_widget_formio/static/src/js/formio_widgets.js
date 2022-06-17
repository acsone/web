odoo.define('web_widget_formio.form_widgets', function (require) {
    "use strict";

    var core = require('web.core');
    var common = require('web.form_common');
    var FieldFormIO = common.AbstractField.extend(common.ReinitializeFieldMixin, {
        template: 'FieldFormIO',
        widget_class: 'field_formio',

        renderElement: function() {
            this._super();
            this.$anchor = this.$el.find("#" +  this.id_for_label)[0];
            this.$jsonPre = this.$el.find("#json-" +  this.id_for_label)[0];
        },

        render_value: function() {
            var value = this.get("value") || '{}';
            var json = JSON.parse(value);
            if (this.get("effective_readonly")) {
                this.form = Formio.createForm(this.$anchor, json);
                this._displayJson(json);
            } else {
                if (json.display == undefined){
                    // only support form at this moment. Should be configurable
                    json.display='form';
                }
                this.builder = new Formio.FormBuilder(this.$anchor, json, this._getBuilderOptions());
                this.builder.instance.on("change", this._onBuilderChange.bind(this));
            }
        },

        _jsonFormat: function(json){
            return JSON.stringify(json, null, 4);
        },

        _onBuilderChange: function(formDef) {
            var json = this.builder.instance.schema
            this._displayJson(json);
            var newJson = this._jsonFormat(json);
            this.internal_set_value(newJson);
        },
        _getBuilderOptions: function () {
        // could be given by attrs attribute on the field element
            return {
                builder: {
                    // hide advanced fields
                    layout: false,
                    data: false,
                    premium: false
                }
            }

        },

        _displayJson: function(json) {
            this.$jsonPre.innerHTML = this._jsonFormat(json);
        },

        set_value: function(value_) {
             this._super(value_);
        },

        get_value: function() {
            return this._super();
        },
    });
    core.form_widget_registry.add('formio', FieldFormIO);

});

/*
var jsonElement = document.getElementById('json');
var formElement = document.getElementById('formio');
var subJSON = document.getElementById('subjson');
var builder = new Formio.FormBuilder(document.getElementById("builder"), {
  display: 'form',
  components: [],
  settings: {
    pdf: {
      "id": "1ec0f8ee-6685-5d98-a847-26f67b67d6f0",
      "src": "https://files.form.io/pdf/5692b91fd1028f01000407e3/file/1ec0f8ee-6685-5d98-a847-26f67b67d6f0"
    }
  }
}, {
  baseUrl: 'https://examples.form.io'
});

var onForm = function(form) {
  form.on('change', function() {
    subJSON.innerHTML = '';
    subJSON.appendChild(document.createTextNode(JSON.stringify(form.submission, null, 4)));
  });
};

var onBuild = function(build) {
  jsonElement.innerHTML = '';
  formElement.innerHTML = '';
  jsonElement.appendChild(document.createTextNode(JSON.stringify(builder.instance.schema, null, 4)));
  Formio.createForm(formElement, builder.instance.form).then(onForm);
};

var onReady = function() {
  var jsonElement = document.getElementById('json');
  var formElement = document.getElementById('formio');
  builder.instance.on('change', onBuild);
};

var setDisplay = function(display) {
  builder.setDisplay(display).then(onReady);
};

// Handle the form selection.
var formSelect = document.getElementById('form-select');
formSelect.addEventListener("change", function() {
  setDisplay(this.value);
});

builder.instance.ready.then(onReady);
*/
