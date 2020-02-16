import { combineEpics } from 'redux-observable';
import { map, ignoreElements, tap } from 'rxjs/operators';
import { createEpic } from 'core/epic';

import { uploadFile, saveRules, getRules } from './api';
import { uploadFileAsync, saveRulesAsync, getRulesAsync } from './action';

const uploadFileEpic = createEpic(uploadFileAsync, data => {
  return uploadFile(data.typeFile, data.file).pipe(ignoreElements());
});

const saveRulesEpic = createEpic(saveRulesAsync, data => {
  return saveRules(data).pipe(ignoreElements());
});

const getRulesEpic = createEpic(getRulesAsync, () => {
  return getRules().pipe(ignoreElements());
});

export const fileEpic = combineEpics(uploadFileEpic, saveRulesEpic, getRulesEpic);
