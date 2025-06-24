import type { Route } from "./+types/home";
import { Welcome } from "../welcome/welcome";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "War" },
    { name: "description", content: "Pick a card!" },
  ];
}

export default function Home() {
  return <Welcome />;
}
