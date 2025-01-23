import { FC } from "react";
import { PokemonProps } from "@/pages/pokemon";
import { getPokemonTypeColorMedium } from "@/utils/pokemonColors";

interface StatsProps {
  pokemon: PokemonProps;
}

const Stats: FC<StatsProps> = ({ pokemon }) => {
  const pokemonBgColor = getPokemonTypeColorMedium(pokemon);

  const renderTypes = () =>
    pokemon.types.map((type, idx) => (
      <div
        key={idx}
        style={{ backgroundColor: pokemonBgColor }}
        className="select-none rounded-md px-2 py-1 text-xs font-bold uppercase tracking-wide text-primary"
      >
        {type.name}
      </div>
    ));

  const renderAbilities = () =>
    pokemon.abilities.map((ability, idx) => (
      <span key={idx} className="mr-2">
        {ability}
        {idx < pokemon.abilities.length - 1 && ","}
      </span>
    ));

  const renderRow = (label: string, value: React.ReactNode) => (
    <tr className="border even:bg-primary-600">
      <td className="border border-secondary/10 p-2 text-left">{label}</td>
      <td className="border border-secondary/10 p-2 text-left">{value}</td>
    </tr>
  );

  return (
    <div className="mt-8 w-full overflow-hidden rounded-lg">
      <table className="w-full border-collapses text-black">
        <thead>
          <tr>
            <th
              colSpan={2}
              className="bg-gray-800 text-white px-5 py-1 text-center text-lg font-semibold text-primary lg:py-2 lg:text-xl"
            >
              Pokemon Stats
            </th>
          </tr>
        </thead>
        <tbody>
          {renderRow(
            "Tipo",
            <div className="flex flex-row items-center justify-center gap-4 text-white">
              {renderTypes()}
            </div>
          )}
          {renderRow("Habilidades", renderAbilities())}
          {renderRow("Altura", `${pokemon.height}m`)}
          {renderRow("Peso", `${pokemon.weight}kg`)}
        </tbody>
      </table>
    </div>
  );
};

export default Stats;
