import React from 'react';
import Link from '@docusaurus/Link';

type Props = {
  index: number; // 1–30
};

const basePath = '/docs/speeches';

const labelFor = (n: number) => `Cadence ${n.toString().padStart(2, '0')}`;

export default function CadenceNav({ index }: Props) {
  const prevIndex = index > 1 ? index - 1 : null;
  const nextIndex = index < 30 ? index + 1 : null;

  const fileFor = (n: number) => `triadicframeworks-cadence-${n}`;

  return (
    <div className="cadence-nav">
      <hr />
      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '1rem' }}>
        <div>
          {prevIndex && (
            <Link to={`${basePath}/${fileFor(prevIndex)}`}>
              ← {labelFor(prevIndex)}
            </Link>
          )}
        </div>
        <div>
          {nextIndex && (
            <Link to={`${basePath}/${fileFor(nextIndex)}`}>
              {labelFor(nextIndex)} →
            </Link>
          )}
        </div>
      </div>
    </div>
  );
}
