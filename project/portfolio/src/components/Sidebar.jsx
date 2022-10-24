import Socials from "./Socials"
import ContactContainer from "./ContactContainer"
import CVContainer from "./CVContainer"

import Avatar from "../img/pfp.jpg"

import "../styles/components/sidebar.sass"

const Sidebar = () => {
   return (
      <aside id="sidebar">
         <img src={Avatar} alt="marcos lott" />
         <p className="title">junior developer at Tesla (UFMG)</p>
         <Socials />
         <ContactContainer />
         <CVContainer />
         
      </aside>
   )
}

export default Sidebar