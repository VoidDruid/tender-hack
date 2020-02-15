import React, { useMemo, useState } from 'react';
import { Line } from 'shared/base/line';
import { Checkbox } from 'shared/base/checkbox';
import { SelectField } from 'shared/fields/selectField';
import { OptionsType } from 'data/model';

import './optionsPanel.scss';

interface Props {
  hideOptions: () => void;
}

export const OptionsPanel: React.FC<Props> = ({ hideOptions }) => {
  const [model, setModel] = useState<OptionsType>({});

  const map = useMemo(() => {
    const a = new Map();
    a.set('a', 'a');
    a.set('b', 'b');
    a.set('c', 'c');
    return a;
  }, []);

  return (
    <Line vertical className="optionsPanel">
      {/* <Checkbox
        text="Is multiple"
        onChange={(value: boolean) => {
          let newModel = { ...model };
          if (value) {
            newModel = { ...newModel, isMultiple: true };
          } else {
            delete newModel.isMultiple;
          }
          setModel(newModel);
        }}></Checkbox> */}
      <div>Parent of</div>
      <SelectField options={map} getLabel={x => x} onChange={() => {}}></SelectField>
      <div onClick={hideOptions} className="hideTip">
        Удалить опции
      </div>
    </Line>
  );
};
