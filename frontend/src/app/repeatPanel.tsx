import React from 'react';
import { ActionType } from 'data/actionTypes';
import { useLoader } from 'core/useLoader';
import { Line } from 'shared/base/line';
import { Button } from 'shared/base/button';

import { Spinner } from './spinner';



interface Props {
  actionType: ActionType;
  action: () => any;
  mod?: string;
}

export const RepeatPanel: React.FC<Props> = ({ actionType, action, mod = undefined, children }) => {
  const item = useLoader(actionType, mod);
  if (item && item.isWait)
    return (
      <Line justifyContent="center" alignItems="center">
        <Spinner />
        <div>
          Loading...
          </div>
      </Line>
    );
  if (item && item.isError)
    return (
      <Line vertical justifyContent="center" alignItems="center">
        <div>Could not load data from the server.</div>
        <div>Press repeat button to reload data.</div>
        <Button buttonType='primary' onClick={action} label='Repeat'>
        </Button>
      </Line>
    );
  return <>{children}</>;
};
