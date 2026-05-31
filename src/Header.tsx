import styles from './Header.module.css'
import Logo from '/favicon.svg'
import Avatar from './assets/icons/inverted/profile.svg'

export function Header() {
    return (
        <>
            <header>
                <div className={styles["left"]}>
                    <div className={styles['nav-menu-button']}>
                        <div id={styles["bar1"]} className={styles["nav-menu-bar"]}></div>
                        <div id={styles["bar2"]} className={styles["nav-menu-bar"]}></div>
                        <div id={styles["bar3"]} className={styles["nav-menu-bar"]}></div>
                    </div>

                    <div className={styles['title']}>
                        <div className={styles['image-wrapper']}>
                            <img src={Logo} alt="" />
                        </div>

                        <h3 className={styles["title-text"]}>
                            Slime
                        </h3>
                    </div>
                </div>

                <div className={styles["center"]}>
                    <nav className={styles['nav-container']}>

                    </nav>
                </div>

                <div className={styles["right"]}>
                    <div className={styles["account"]}>
                        <div className={styles["account-avatar"]}>
                            <img src={Avatar} alt="" />
                        </div>
                    </div>
                </div>
            </header>
        </>
    )
}