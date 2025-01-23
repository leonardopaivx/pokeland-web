/* eslint-disable react/jsx-key */
import Image from "next/image";
import logoImage from "@/assets/images/Logo.png";

const Navbar = () => {
  return (
    <header className="fixed inset-x-0 top-0 z-50 h-14 w-full bg-primary px-3 shadow-md shadow-secondary/20  flex items-center justify-center bg-gray-50 dark:bg-gray-900">
      <div className="flex  max-w-7xl flex-row items-center">
        <Image src={logoImage} alt="pokeball" width={100} />
      </div>
    </header>
  );
};

export default Navbar;
