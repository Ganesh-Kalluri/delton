/** @leewise-module **/

import { TimesheetTimerKanbanRenderer } from "@timesheet_grid/views/timesheet_kanban/timesheet_timer_kanban_renderer";
import { TimesheetLeaderboard } from "@sale_timesheet_enterprise/components/timesheet_leaderboard/timesheet_leaderboard";

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { onWillStart } from "@leewise/owl";

patch(TimesheetTimerKanbanRenderer, {
    components: {
        ...TimesheetTimerKanbanRenderer.components,
        TimesheetLeaderboard,
    },
});

patch(TimesheetTimerKanbanRenderer.prototype, {
    setup() {
        super.setup()
        this.user = useService('user');
        onWillStart(async () => {
            this.userHasBillingRateGroup = await this.user.hasGroup("sale_timesheet_enterprise.group_timesheet_leaderboard_show_rates");
        });
    },

    get isMobile() {
        return this.env.isSmall;
    },
});
