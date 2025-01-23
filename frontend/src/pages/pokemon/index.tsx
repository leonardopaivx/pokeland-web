import PokemonImage from "@/components/PokeImage";
import PokemonStats from "@/components/PokemonStats";
import { useEffect, useRef, useState } from "react";
import { fetchCatchPokemon } from "@/pages/api/api";
import { toast } from "react-toastify";
import JSConfetti from "js-confetti";
import Lottie from "lottie-react-web";
import PokeLoading from "@/assets/gifs/pokeLoading.json";

export interface PokemonTypesProps {
  name: string;
  url: string;
}

export interface PokemonProps {
  id: number;
  name: string;
  height: number;
  weight: number;
  abilities: string[];
  types: PokemonTypesProps[];
  sprites: {
    front_default: string;
    back_default: string;
  };
}

const PokemonPage: React.FC = () => {
  const [pokemonCatched, setpokemonCatched] = useState<
    PokemonProps | undefined
  >(undefined);
  const [isLoading, setIsLoading] = useState(false);
  const jsConfettiRef = useRef<JSConfetti | null>(null);

  useEffect(() => {
    if (typeof window !== "undefined") {
      jsConfettiRef.current = new JSConfetti();
    }
  }, []);

  const handleCatchPokemon = async () => {
    setIsLoading(true);
    try {
      const pokemonData = await fetchCatchPokemon();
      setpokemonCatched(pokemonData);

      toast.success(`Você capturou ${pokemonData.name}!`);

      if (jsConfettiRef.current) {
        jsConfettiRef.current.addConfetti();
      }
    } catch {
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex h-screen w-full justify-center p-5 lg:mt-20 bg-gray-50 dark:bg-gray-700">
      <div className="flex flex-col items-center">
        <button
          onClick={handleCatchPokemon}
          disabled={isLoading}
          className="mb-5 bg-orange-700 text-white text-xl w-80 h-16 flex items-center justify-center rounded-lg font-bold shadow hover:bg-orange-600 disabled:bg-gray-400 transition-all duration-200 ease-in-out"
        >
          {isLoading ? (
            <Lottie
              options={{ animationData: PokeLoading }}
              style={{ width: "50%", height: "50%" }}
            />
          ) : (
            "Capturar Pokémon"
          )}
        </button>

        {pokemonCatched && (
          <div className="mx-auto grid w-lg lg:max-w-[60vw] lg:w-[60vw] grid-cols-1 overflow-hidden rounded-2xl shadow-lg shadow-secondary/20 lg:max-h-[70vh] lg:mt-5 lg:grid-cols-2 bg-white">
            <PokemonImage pokemon={pokemonCatched} />
            <PokemonStats pokemon={pokemonCatched} />
          </div>
        )}
      </div>
    </div>
  );
};

export default PokemonPage;
