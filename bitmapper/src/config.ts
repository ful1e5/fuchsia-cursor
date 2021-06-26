import { Colors } from "./core/types";

interface Config {
  themeName: string;
  color: Colors;
}

const fucshia = "#FF00FF";
const white = "#FFFFFF";

const config: Config[] = [
  {
    themeName: "Fucshia",
    color: {
      base: fucshia,
      outline: white,
    },
  },
];

export { config };
