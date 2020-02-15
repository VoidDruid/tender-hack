import { combineEpics } from 'redux-observable';

import { fileEpic } from './file/epic';

export const rootEpic = combineEpics(fileEpic);
