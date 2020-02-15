import { combineEpics } from 'redux-observable';
import { map, ignoreElements } from 'rxjs/operators';
import { createEpic } from 'core/epic';

import { uploadFile } from './api';
import { uploadFileAsync } from './action';

const uploadFileEpic = createEpic(uploadFileAsync, data => {
  return uploadFile(data.typeFile, data.file).pipe(ignoreElements());
});

export const fileEpic = combineEpics(uploadFileEpic);
