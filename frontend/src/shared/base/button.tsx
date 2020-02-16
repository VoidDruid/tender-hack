import React from 'react';
import classNames from 'classnames';

import { Line } from './line';
import { Icon } from './icon';
import { SpaceProps, propsToSpace } from './utils/spaceUtil';

export interface ButtonProps extends SpaceProps, React.HTMLAttributes<any> {
  label?: string;
  icon?: 'vk' | 'google' | 'twitter';
  buttonType: 'light' | 'primary';
  className?: string;
  onClick?: () => void;
  disabled?: boolean;
}

export const Button: React.FC<ButtonProps> = ({ disabled, label, icon, buttonType, className, onClick, ...other }) => {
  const classes = classNames('btn', { [`btn-${buttonType}`]: true }, propsToSpace(other), className);
  return (
    <div className="buttons">
      <button disabled={disabled} className={classes} onClick={onClick}>
        <Line>
          <div>{icon ? <Icon name={icon} prefix="fab"></Icon> : null}</div>
          <div>{label ? <div className="label">{label}</div> : null}</div>
        </Line>
      </button>
    </div>
  );
};
