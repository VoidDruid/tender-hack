import { library } from '@fortawesome/fontawesome-svg-core';
//regular
import { faSquare } from '@fortawesome/free-regular-svg-icons/faSquare';
import { faCheckSquare } from '@fortawesome/free-regular-svg-icons/faCheckSquare';
//solid
import { faAngleRight } from '@fortawesome/free-solid-svg-icons/faAngleRight';
import { faArrowRight } from '@fortawesome/free-solid-svg-icons/faArrowRight';
import { faTimes } from '@fortawesome/free-solid-svg-icons/faTimes';
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

library.add(
  //regular
  faSquare,
  faCheckSquare,
  //solid
  faAngleRight,
  faArrowRight,
  faTimes
);

export type ImportedIcon =
  | 'check-square'
  | 'square'
  | 'angle-right'
  | 'google'
  | 'vk'
  | 'twitter'
  | 'arrow-right'
  | 'times';

export interface Props extends React.HTMLAttributes<any> {
  className?: string;
  spin?: boolean;
  prefix?: 'fas' | 'far' | 'fab';
  name: ImportedIcon;
}

export const Icon: React.FC<Props> = ({ prefix = 'fas', name, spin, className, ...other }) => {
  return <FontAwesomeIcon icon={[prefix, name]} spin={spin} {...other}></FontAwesomeIcon>;
};
