import { Colors } from "./core/types";

interface Config {
  themeName: string;
  color: Colors;
}

const fuchsia = "#FF00FF";
const white = "#FFFFFF";

const config: Config[] = [
  {
    themeName: "Fuchsia",
    color: {
      base: fuchsia,
      outline: white,
    },
  },
];

export { config };
