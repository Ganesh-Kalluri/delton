/** @leewise-module **/

import { Component } from "@leewise/owl";

export class Tooltip extends Component {}
Tooltip.template = "web.Tooltip";
Tooltip.props = {
    close: Function,
    tooltip: { type: String, optional: true },
    template: { type: String, optional: true },
    info: { optional: true },
};
