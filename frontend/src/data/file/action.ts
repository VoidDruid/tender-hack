import { createAction } from 'core/redux';
import { ActionType } from 'data/actionTypes';
import { RuleType } from 'data/file/models';

export const uploadFileAsync = createAction<{ typeFile: string; file: File }>(ActionType.FILE_UPLOADFILE);
export const saveRulesAsync = createAction<RuleType[]>(ActionType.FILE_SAVERULES);
export const getRulesAsync = createAction(ActionType.FILE_GETRULES);
