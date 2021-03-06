import { createAction } from 'core/redux';
import { ActionType } from 'data/actionTypes';
import { RuleType } from 'data/file/models';

export const uploadFileAsync = createAction<{ id: number; file: FormData }>(ActionType.FILE_UPLOADFILE);
export const saveRulesAsync = createAction<RuleType[]>(ActionType.FILE_SAVERULES);
export const getRulesAsync = createAction(ActionType.FILE_GETRULES);
export const setFile = createAction<string>(ActionType.FILE_SETFILE);
