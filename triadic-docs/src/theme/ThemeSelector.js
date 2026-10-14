import React from 'react';
import {useColorMode} from '@docusaurus/theme-common';

export default function ThemeSelector() {
  const {setColorMode} = useColorMode();

  React.useEffect(() => {
    const now = new Date();
    const day = now.getDay(); // 0 = Sunday, 6 = Saturday
    const date = now.getDate(); // 1–31

    // Weekend rule (Sat/Sun = Theme A)
    const weekendMode = (day === 0 || day === 6);

    // Odd/even rule (odd = Theme A)
    const oddMode = (date % 2 === 1);

    // Choose your rule:
    const useWeekendRule = true;

    const themeA = weekendMode || oddMode;
    const themeB = !themeA;

    if (useWeekendRule) {
      setColorMode(weekendMode ? 'dark' : 'light');
    } else {
      setColorMode(oddMode ? 'dark' : 'light');
    }
  }, []);

  return null;
}
