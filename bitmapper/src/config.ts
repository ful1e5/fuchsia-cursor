import { Colors } from "./core/types";

interface Config {
  themeName: string;
  color: Colors;
}

const fuchsia = "#e11c79";
const pop = "#f8b572";
const white = "#ffffff";
const red = "#ff0000";

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
  {
    themeName: "Fuchsia-Red",
    color: {
      base: red,
      outline: white,
    },
  },
];

export { config };
