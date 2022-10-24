import {AiFillPhone, AiOutlineMail, AiFillEnvironment} from 'react-icons/ai'

import '../styles/components/contactcontainer.sass'

const ContactContainer = () => {
   return (
      <section id="information">
         <div className='info-card'>
            <AiFillPhone id='phone-icon' />
            <div>
               <h3>phone number</h3>
               <p>+55 31 99503-0620</p>
            </div>
         </div>
         <div className='info-card'>
            <AiOutlineMail id='email-icon' />
            <div>
               <h3>email</h3>
               <p>lott.marcos@gmail.com</p>
            </div>
         </div>
         <div className='info-card'>
            <AiFillEnvironment id='pin-icon' />
            <div>
               <h3>place</h3>
               <p>Belo Horizonte - Brazil</p>
            </div>
         </div>
      </section>
   )
}

export default ContactContainer