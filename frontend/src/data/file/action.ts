import { createAction } from 'core/redux';
import { ActionType } from 'data/actionTypes';

export const uploadFileAsync = createAction<{ typeFile: string; file: File }>(ActionType.FILE_UPLOADFILE);
