import { Colors } from "./core/types";

interface Config {
  themeName: string;
  color: Colors;
}

const fucshia = "#FF00FF";

const config: Config[] = [
  {
    themeName: "Fucshia",
    color: {
      base: fucshia,
      outline: fucshia,
    },
  },
];

export { config };
