import { combineReducers } from 'redux';
import { loaderReducer } from 'core/loader';

import { fileReducer } from './file/reducer';

export const rootReducer = combineReducers({
    loader: loaderReducer,
    file: fileReducer
});
