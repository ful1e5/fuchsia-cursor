import { Colors } from "./core/types";

interface Config {
  themeName: string;
  color: Colors;
}

const fuchsia = "#e11c79";
const pop = "#f8b572";
const white = "#ffffff";

const config: Config[] = [
  {
    themeName: "Fuchsia",
    color: {
      base: fuchsia,
      outline: white,
    },
  },
  {
    themeName: "Fuchsia-Pop!",
    color: {
      base: pop,
      outline: white,
    },
  },
];

export { config };
