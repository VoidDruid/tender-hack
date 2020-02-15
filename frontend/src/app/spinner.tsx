import React from 'react';
import classNames from 'classnames';


interface Props {
  className?: string;
  small?: boolean;
}

export const Spinner: React.FC<Props> = ({ className, small, ...other }) => {
  const classes = classNames('spinner-border', { 'spinner-border-sm': small }, className);
  return (
    <div className={classes} role="status" {...other}>
      <span className="sr-only"></span>
    </div>
  );
};
