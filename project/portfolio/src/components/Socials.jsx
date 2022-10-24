import {FaLinkedinIn, FaGithub, FaInstagram} from 'react-icons/fa'

import '../styles/components/socials.sass'

const socials_array = [
   { name: "linkedin", icon: <FaLinkedinIn />, link: "https://www.linkedin.com/in/lott-marcos/" },
   { name: "github", icon: <FaGithub />, link: "https://www.github.com/lottmarcos/" },
   { name: "instagram", icon: <FaInstagram />, link: "https://www.instagram.com/lott.marcos/"},
]

const Socials = () => {
   return (
      <section id="socials">
         {socials_array.map((network) => (
            <a href={network.link} className='social-btn' id={network.name} key={network.name}>
               {network.icon}
            </a>
         ))}
      </section>
   )
}

export default Socials