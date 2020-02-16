import React, { useState, useCallback } from 'react';

import './checkbox.scss';

import { Line } from './line';
import { Icon } from './icon';

export interface CheckboxProps {
  text?: string;
  onChange: (value: boolean) => void;
}

export const Checkbox: React.FC<CheckboxProps> = ({ text, onChange }) => {
  const [isChecked, setIsChecked] = useState(false);

  const onChangeCallback = useCallback(() => {
    onChange(!isChecked);
    setIsChecked(!isChecked);
  }, [isChecked]);

  return (
    <Line alignItems="center" className="auth-checkbox">
      <Icon name={isChecked ? 'check-square' : 'square'} prefix="far" onClick={onChangeCallback}></Icon>
      <div className="text">{text}</div>
    </Line>
  );
};
