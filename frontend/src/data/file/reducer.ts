import { createReducer } from 'core/redux';

interface FileInitialState {

}

const initialState: () => FileInitialState = () => ({
});

export const fileReducer = createReducer(initialState, {
});
