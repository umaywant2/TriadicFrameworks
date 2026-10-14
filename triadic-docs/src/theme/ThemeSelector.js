import ExecutionEnvironment from '@docusaurus/ExecutionEnvironment';

let ThemeSelector = function () {
  return null;
};

if (ExecutionEnvironment.canUseDOM) {
  // Only import React + useColorMode in the browser
  const React = require('react');
  const {useColorMode} = require('@docusaurus/theme-common');

  ThemeSelector = function () {
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
  };
}

export default ThemeSelector;
