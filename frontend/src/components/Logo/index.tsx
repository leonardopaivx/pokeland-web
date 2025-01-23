import Image from "next/image";
import logoImage from "@/assets/images/Logo.png";

const Logo = () => {
  return (
    <a
      href=""
      className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white"
    >
      {/* <Lottie
        options={{ animationData: PokeLoading }}
        style={{ width: "20%" }}
      /> */}
      <Image src={logoImage} alt="pokeball" width={400} />
    </a>
  );
};

export default Logo;
