import React from 'react';
import ReactDOM from 'react-dom';
import { App } from 'app/app';
import { Provider } from 'react-redux';
import { store } from 'core/store';

import './base.scss';

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
