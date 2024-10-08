/** @leewise-module */

import { Model } from "@leewise/o-spreadsheet";
import { DataSources } from "@spreadsheet/data_sources/data_sources";
import { migrate } from "@spreadsheet/o_spreadsheet/migration";

/**
 * Convert PIVOT functions from relative to absolute.
 *
 * @param {import("@web/env").LeewiseEnv} env
 * @param {object} data
 * @returns {Promise<object>} spreadsheetData
 */
export async function convertFromSpreadsheetTemplate(env, data, revisions) {
    const model = new Model(
        migrate(data),
        { custom: { dataSources: new DataSources(env) } },
        revisions
    );
    await model.config.custom.dataSources.waitForAllLoaded();
    const proms = [];
    for (const pivotId of model.getters.getPivotIds()) {
        proms.push(model.getters.getPivotDataSource(pivotId).prepareForTemplateGeneration());
    }
    await Promise.all(proms);
    model.dispatch("CONVERT_PIVOT_FROM_TEMPLATE");
    return model.exportData();
}
