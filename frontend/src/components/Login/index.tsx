import { useState } from "react";
import { useRouter } from "next/router";
import Lottie from "lottie-react-web";
import PokeLoading from "@/assets/gifs/pokeLoading.json";
import Link from "next/link";
import { toast } from "react-toastify";
import { fetchLogin } from "@/pages/api/api";
import { LoginComponentI } from "@/types/LoginTypes";

interface LoginComponentProps {
  id?: string;
}

const LoginComponent = ({}: LoginComponentProps) => {
  const [loginInfos, setLoginInfos] = useState<LoginComponentI>(
    {} as LoginComponentI
  );
  const [loginLoading, setLoginLoading] = useState<boolean>(false);
  const { username, password } = loginInfos;

  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!username || !password) {
      toast.error("Por favor, preencha todos os campos.");
      return;
    }

    setLoginLoading(true);

    try {
      await fetchLogin(loginInfos);
      router.push("/pokemon");
    } catch {
      // Intencionalmente vazio
    } finally {
      setLoginLoading(false);
    }
  };

  return (
    <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
      <div className="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
          Faça login e torne-se o melhor Treinador Pokémon!
        </h1>
        <form className="space-y-4 md:space-y-6" onSubmit={handleSubmit}>
          <div>
            <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
              username
            </label>
            <input
              type="text"
              name="username"
              id="username"
              className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="username"
              required={true}
              value={username}
              onChange={(e) =>
                setLoginInfos({ ...loginInfos, username: e.target.value })
              }
            />
          </div>
          <div>
            <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
              senha
            </label>
            <input
              type="password"
              name="password"
              id="password"
              placeholder="••••••••"
              className="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              required={true}
              value={password}
              onChange={(e) =>
                setLoginInfos({ ...loginInfos, password: e.target.value })
              }
            />
          </div>
          <div className="flex items-center justify-between">
            <div className="flex items-start">
              <div className="flex items-center h-5">
                <input
                  id="remember"
                  aria-describedby="remember"
                  type="checkbox"
                  className="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
                />
              </div>
              <div className="ml-3 text-sm">
                <label className="text-gray-500 dark:text-gray-300">
                  Lembrar de mim
                </label>
              </div>
            </div>
            <a
              href="#"
              className="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500"
            >
              Esqueceu a senha?
            </a>
          </div>
          <button
            type="submit"
            className="w-full text-gray-500 dark:text-gray-400 bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
          >
            {loginLoading ? (
              <Lottie
                options={{ animationData: PokeLoading }}
                style={{ width: "10%" }}
              />
            ) : (
              "Entrar"
            )}
          </button>
          <p className="text-sm font-light text-gray-500 dark:text-gray-400">
            Ainda não possui sua conta?{" "}
            <Link
              href="/register"
              className="font-medium text-primary-600 hover:underline dark:text-primary-500"
            >
              Registrar
            </Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default LoginComponent;
