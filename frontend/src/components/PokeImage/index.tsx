import { PokemonProps } from "@/pages/pokemon";
import { getPokemonTypeColorMedium } from "@/utils/pokemonColors";

interface PokemonImageProps {
  pokemon: PokemonProps;
}

const PokemonImage = ({ pokemon }: PokemonImageProps) => {
  const pokemonBgColor = getPokemonTypeColorMedium(pokemon);

  return (
    <div
      className="relative flex h-full max-h-[70vh] min-h-[50vh] w-full flex-col items-center justify-between overflow-hidden rounded-2xl lg:rounded-br-none"
      style={{
        background: `radial-gradient(#fafafa,30%, ${pokemonBgColor})`,
      }}
    >
      <div className="flex w-full flex-row items-center justify-between p-5">
        <p className="select-none text-4xl font-bold tracking-widest text-primary/70 drop-shadow-2xl">
          {`#${pokemon.id.toString().padStart(3, "0")}`}
        </p>
      </div>

      <div className="absolute top-28 flex select-none flex-col items-center justify-center text-4xl font-bold tracking-widest text-primary opacity-100 drop-shadow-xl lg:top-36 lg:text-7xl">
        <h1 className="capitalize">{pokemon.name}</h1>
      </div>

      <div className="relative flex h-2/4 w-2/4 items-center justify-center lg:mt-36 lg:h-full lg:w-80">
        <img
          key={pokemon.id}
          src={pokemon.sprites.front_default}
          alt={pokemon.name}
          width={200}
          height={200}
          className="h-full w-full animate-poke-bounce object-contain"
        />
      </div>
    </div>
  );
};

export default PokemonImage;
