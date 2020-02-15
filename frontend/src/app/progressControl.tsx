import React from 'react';
import { Line } from 'shared/base/line';
import { Icon } from 'shared/base/icon';

import './progressControl.scss';

export const ProgressControl: React.FC = () => {
  return (
    <Line className="progressControl">
      <Line className="card container" justifyContent="around" alignItems="center">
        <div>Загрузка файла</div>
        <Icon name="arrow-right"></Icon>
        <div>Задание параметров</div>
        <Icon name="arrow-right"></Icon>
        <div>Выгрузка файла</div>
      </Line>
    </Line>
  );
};
