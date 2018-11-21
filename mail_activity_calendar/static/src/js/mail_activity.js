odoo.define('calendar.Activity', function (require) {
"use strict";

var Activity = require('mail.Activity');
var Dialog = require('web.Dialog');
var core = require('web.core');
var Model = require('web.Model');
var _t = core._t;

Activity.include({

    /**
     * Override behavior to redirect to calendar event instead of activity
     *
     * @override
     */
    _onEditActivity: function (event, options) {
        var self = this;
        var activity_id = $(event.currentTarget).data('activity-id');
        var activity = _.find(this.activities, function (act) { return act.id === activity_id; });
        if (activity && activity.activity_category === 'meeting' && activity.calendar_event_id) {
            return self._super(event, _.extend({
                res_model: 'calendar.event',
                res_id: activity.calendar_event_id[0],
            }));
        }
        return self._super(event, options);
    },

    /**
     * Override behavior to warn that the calendar event is about to be removed as well
     *
     * @override
     */
    _onUnlinkActivity: function (event, options) {
        event.preventDefault();
        var self = this;
        var activity_id = $(event.currentTarget).data('activity-id');
        var activity = _.find(this.activities, function (act) { return act.id === activity_id; });
        if (activity && activity.activity_category === 'meeting' && activity.calendar_event_id) {
            var done = $.Deferred();
            Dialog.confirm(
                self,
                _t("The activity is linked to a meeting. Deleting it will remove the meeting as well. Do you want to proceed ?"), {
                    confirm_callback: function () {
                        new Model('mail.activity')
                            .call('unlink_w_meeting', [[activity_id]])
                            .then(function(res) {
                                self.render_value();
                                done.resolve(res);
                            });
                    },
                }
            );
            return done;
        }
        else {
            return self._super(event, options);
        }
    },
});

});
