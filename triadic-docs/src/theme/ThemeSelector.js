import React from 'react';
import {useColorMode} from '@docusaurus/theme-common';
import ExecutionEnvironment from '@docusaurus/ExecutionEnvironment';

export default function ThemeSelector() {
  // Prevent SSR entirely
  if (!ExecutionEnvironment.canUseDOM) {
    return null;
  }

  const {setColorMode} = useColorMode();

  React.useEffect(() => {
    const now = new Date();
    const day = now.getDay(); // 0 = Sunday, 6 = Saturday
    const date = now.getDate(); // 1–31

    const weekendMode = (day === 0 || day === 6);
    const oddMode = (date % 2 === 1);

    const useWeekendRule = true;

    if (useWeekendRule) {
      setColorMode(weekendMode ? 'dark' : 'light');
    } else {
      setColorMode(oddMode ? 'dark' : 'light');
    }
  }, []);

  return null;
}
