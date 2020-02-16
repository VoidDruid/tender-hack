import { createReducer } from 'core/redux';
import { ActionType } from 'data/actionTypes';

interface FileInitialState {
  file: string;
}

const initialState: () => FileInitialState = () => ({ file: '' });

export const fileReducer = createReducer(initialState, {
  [ActionType.FILE_SETFILE]: 'file'
});
