import ftplib


def main():
    host = input ( "Enter the host: " )
    annonLogin ( host ) 


def annonLogin ( hostname ):
    
    try:
        hostname = ftplib.FTP ( hostname )
    
        ftp.login ( 'annonymous', 'me@yours.com' )

        print ( "Login successful" )

    except:
        print ( "Login failed" )

main()
