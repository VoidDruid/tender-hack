import React from 'react';
import { Line } from 'shared/base/line';
import { UploadZone } from 'app/uploadZone';
import { ProgressControl } from 'app/progressControl';
import { DownloadZone } from 'app/downloadZone';
import { ProcessControl } from 'app/processControl';

import './app.scss';

export const App: React.FC = () => {
  return (
    <Line justifyContent="between" className="app">
      <Line vertical className="leftPanel">
        <ProgressControl />
        <UploadZone />
        <DownloadZone />
      </Line>
      <Line className="rightPanel">
        <ProcessControl />
      </Line>
    </Line>
  );
};
