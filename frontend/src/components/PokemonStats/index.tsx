import { PokemonProps } from "@/pages/pokemon";
import Stats from "../Stats";

interface PokemonStatsProps {
  pokemon: PokemonProps;
}

const PokemonStats = ({ pokemon }: PokemonStatsProps) => {
  return (
    <div className="overscroll-visible flex h-full w-full flex-col items-center justify-start bg-primary lg:max-h-[70vh] lg:overflow-y-auto">
      <div className="p-5">
        <Stats pokemon={pokemon} />
      </div>
    </div>
  );
};

export default PokemonStats;
