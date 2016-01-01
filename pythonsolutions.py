# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$17-Dec-2015 7:20:56 PM$"

import sys

if __name__ == "__main__":
    print("Please enter the day of the puzzle to solve(4, 5, 6 or 7):")
    command = input('--> ')
    if command == '4':
        import hashlib
        #begin by getting the puzzle number
        checkString = ''
        while checkString == '':
            print('Enter puzzle number(1 or 2):')
            puzzleNum = input('--> ')
            if puzzleNum == '1':
                checkNumber = 5
                checkString = '00000'
            elif puzzleNum == '2':
                checkNumber = 6
                checkString = '000000'
                
                
        secretKey = "yzbqklnj"
        hashSuffixNum = 0
        hashResult = ''
        while hashResult[0:checkNumber] != checkString:
            hashSuffixNum = hashSuffixNum+1
            fullKey = secretKey.encode('utf-8')+str(hashSuffixNum).encode('utf-8')
            hashCalc = hashlib.md5()
            hashCalc.update(fullKey)
            hashResult = hashCalc.hexdigest()
        print("Lowest number is: "+str(hashSuffixNum))
        print("Full Key: "+str(fullKey))
        
        
    elif command == '5':
        import re
        ThreeVowelRe = re.compile("[a,e,i,o,u].*[a,e,i,o,u].*[a,e,i,o,u]")
        TwoInARowRe = re.compile(r'([a-z])\1{1,}')
        DisallowedStrings = re.compile("(ab)|(cd)|(pq)|(xy)")
        
        #puzzleTwo regex
        MatchWithOneBetween = re.compile(r'([a-z]).\1')
        MatchTwoPairs = re.compile(r'([a-z][a-z]).*\1')
        
        niceStrings = 0
#        entryString = "uurcxstgmygtbstg"
        entryString = "rthkunfaakmwmush_qxlnvjguikqcyfzt_sleaoasjspnjctqt_lactpmehuhmzwfjl_bvggvrdgjcspkkyj_nwaceixfiasuzyoz_hsapdhrxlqoiumqw_lsitcmhlehasgejo_hksifrqlsiqkzyex_dfwuxtexmnvjyxqc_iawwfwylyrcbxwak_mamtkmvvaeeifnve_qiqtuihvsaeebjkd_skerkykytazvbupg_kgnxaylpgbdzedoo_plzkdktirhmumcuf_pexcckdvsrahvbop_jpocepxixeqjpigq_vnsvxizubavwrhtc_lqveclebkwnajppk_ikbzllevuwxscogb_xvfmkozbxzfuezjt_ukeazxczeejwoxli_tvtnlwcmhuezwney_hoamfvwwcarfuqro_wkvnmvqllphnsbnf_kiggbamoppmfhmlf_ughbudqakuskbiik_avccmveveqwhnjdx_llhqxueawluwmygt_mgkgxnkunzbvakiz_fwjbwmfxhkzmwtsq_kzmtudrtznhutukg_gtvnosbfetqiftmf_aoifrnnzufvhcwuy_cldmefgeuwlbxpof_xdqfinwotmffynqz_pajfvqhtlbhmyxai_jkacnevnrxpgxqal_esxqayxzvortsqgz_glfoarwvkzgybqlz_xdjcnevwhdfsnmma_jyjktscromovdchb_pvguwmhdvfxvapmz_iheglsjvxmkzgdbu_lwjioxdbyhqnwekv_zcoguugygkwizryj_ogvnripxxfeqpxdh_hkvajhsbfnzsygbm_cnjqeykecopwabpq_wojjtbcjinoiuhsj_kpwpvgxbyzczdzjq_wrvhylisemlewgzk_uiezkmnhilfzahtm_mucteynnuxpxzmvt_zaiwbgxefusfhmst_apptbogpxivjwink_qryboarjtwjhjgjb_irehxupgyseaahzd_fobstqxguyubggoh_ysriumfghtxtfxwe_auchdmasvfeliptw_mztuhefcrnknyrdl_tyjmkhihbwabjtaa_yquzkdtgsljkaebw_almvdvofjtkyzbmd_emqftiuqqpdwwbrv_hrrhmqfpepvbawvw_atrkgykycvgxbpyb_dhthetnealksbdan_zzqafhgicubptiyo_qdtaieaziwhbttnw_kyskgapdgqrtrefw_edwzlpqztpydmdlr_awszjnlmvlyqsuvl_kcrtmtshtsgixvcp_jtaskgkijivbbkri_mmggfwapsetemiuj_itagrrnjbnmhgppd_uqmbezechbrpbnqq_nnyimvtascflpzsa_knqeimypkdttyudj_vgoiyvtvegwyxjjd_qubzdxsbecktzrho_zehojtvktsbbxijb_xepmjrekwcgoxyoh_bnptxnocbpbqbyeq_sfvynsywscbnymos_dsltfbpcmffbluba_kncrlzlmkikylppa_siwudrvmildgaozv_jhhefbvbvneqzvtc_lqjgztxitbuccqbp_himmwlbhjqednltt_vwognchyertnnfil_eejakhapkbodrntf_qxuijkkhhlskgrba_aankpfxxicfpllog_vuxykvljyqexfhrn_epgygflbxlbwybzq_zuxmwvetmvcszayc_xttwhfqmemgtjnkf_hftwldmivyfunfvl_bejlyxfamzliilrj_zkehazcxyyvtrxti_dsgafehmcfpycvgz_igremmqdojqdvwmb_swnjzvmhcslvkmiw_fchzbfbmtqtxmaef_xwjmyyrlznxrcytq_brwcwzpcvbwdrthl_fvrlridacsiojdmb_mhsturxdlmtxozvy_usxvqyrwywdyvjvz_gwazuslvmarfpnzm_rgkbudaqsnolbcqo_dpxvlbtavdhdedkj_nnqmjzejhodyfgyd_ozoazxkfhujgtzvy_psdgvhzdiwnuaxpl_tznkilxpogbzgijz_wnpytcseirtborhh_lhauurlfsmagfges_oqfbzixnlywkzwwy_yoehapoyjpakziom_vtjftdcsfdzbmtrn_zcshfnodiwixcwqj_wapbxpaxgjvtntkm_qfyypkyvblrtaenh_bsxhbxkovgukhcza_kitdmvpiwzdonoyy_slkbhxmehzavbdsf_dovzjouqkzkcmbkl_qpbigdcqkfnfkxvq_eaiaquhnesvtcdsv_mhbezlhqojdsuryj_dqprkkzxlghkoccx_xqepmorryeivhrhm_frwmrjpezwmjflvf_gjpfgwghodfslwlf_fzyvajisdjbhfthq_pvzxkxdscdbilrdb_mtaxmqcnagmplvnm_rlyafujuuydrqwnc_gvqvrcxwyohufehq_lmrkircgfrfusmfd_ovlpnkxcpimyaspb_xhyjremmqhdqywju_pxfczlhpzbypfarm_utjhprzhtggausyp_utzkkzlnyskjtlqh_cecbcnxpazvkedic_xwvoaggihrbhmijq_krredhmtwlfmyagw_lwfhxgbknhwudkzw_vyczyvuxzmhxmdmn_swcoaosyieqekwxx_waohmlfdftjphpqw_gaclbbfqtiqasijg_ybcyaxhluxmiiagp_xgtxadsytgaznndw_wzqhtjqpaihyxksm_fdwltsowtcsmsyhm_rpoelfbsararhfja_tswgdacgnlhzwcvz_xjgbhdlxllgeigor_ksgthvrewhesuvke_whgooqirdjwsfhgi_toztqrxzavxmjewp_hbkayxxahipxnrtl_lazimkmdnhrtflcu_ndoudnupbotwqgmr_niwuwyhnudxmnnlk_hlmihzlrpnrtwekr_wzkttdudlgbvhqnc_rfyzzgytifkqlxjx_skddrtwxcyvhmjtb_mljspkvjxbuyhari_xwkhozaoancnwaud_nookruxkdffeymdz_oiqfvpxmcplyfgoa_qoxggshmrjlzarex_lsroezewzkrwdchx_nkoonmvdydgzspcl_lygxeqztdqklabov_jempjyzupwboieye_hpdaqkhjiddzybly_cvcizjlnzdjfjlbh_vaaddsbkcgdjhbkj_pjxmtxoyrkmpnenf_ujqdvyqnkbusxlps_miyvzkzqploqaceb_gapcsbkulicvlnmo_xqpcyriqhjhaeqlj_ipumdjwlldzqhmgh_swdstecnzttmehxe_ucmqordmzgioclle_aywgqhmqlrzcxmqx_ptkgyitqanvjocjn_wcesxtmzbzqedgfl_rnetcouciqdesloe_chpnkwfdjikqxwms_onpyrjowcuzdtzfg_tydnqwaqwkskcycz_dhamguhmkjzzeduy_oecllwyrlvsyeeuf_gsukajpoewxhqzft_sgdnffdixtxidkih_pqqzjxzydcvwwkmw_wnjltltufkgnrtgm_hylaicyfrqwolnaq_ovfnugjjwyfjunkm_xknyzsebmqodvhcl_uwfmrjzjvvzoaraw_zaldjvlcnqbessds_zphvjuctrsksouvz_ceqbneqjwyshgyge_wmelhaoylbyxcson_nghuescieaujhgkj_dhjmflwwnskrdpph_exvanqpoofjgiubf_aidkmnongrzjhsvn_mdbtkyjzpthewycc_izctbwnzorqwcqwz_hrvludvulaopcbrv_mrsjyjmjmbxyqbnz_sjdqrffsybmijezd_geozfiuqmentvlci_duzieldieeomrmcg_ehkbsecgugsulotm_cymnfvxkxeatztuq_bacrjsgrnbtmtmdl_kbarcowlijtzvhfb_uwietqeuupewbjav_ypenynjeuhpshdxw_fwwqvpgzquczqgso_wjegagwkzhmxqmdi_vocvrudgxdljwhcz_nnytqwspstuwiqep_axapfrlcanzgkpjs_lklrjiszochmmepj_gxadfpwiovjzsnpi_qidsjxzgwoqdrfie_wgszciclvsdxxoej_kwewlmzxruoojlaq_ywhahockhioribnz_ucbqdveieawzucef_mdyyzmfoaxmzddfv_hsxnabxyqfzceijv_vivruyvbrtaqeebr_jxfeweptjtgvmcjc_mmypqxmpurhculwd_mpiaphksvctnryli_xqzqnuxmuzylkkun_fndmtefjxxcygtji_dnorqlldvzqprird_nutokyajmjpwjaqu_vlupfperqyqkjcaj_dgihjeokrphkpdnk_nvbdyrlheqzixuku_mhrkntnxvsmvrpka_kvhkyanlhhymwljf_fhipumtegqfgeqqw_vpfjgveycdefuabu_kzincljffncylcsf_tsezxymwmjtyegqw_wxhcdrqedkdcwxli_ueihvxviirnooomi_kfelyctfvwyovlyh_horzapuapgtvzizz_iiqkdpmfvhwwzmtj_rsaclclupiicstff_quwkkhrafypkaoum_gyrgkgmwqfkeudfe_noydhbqacwptyfmy_efwwuipzgtkwffhf_suyojcitomdxsduh_lbcxnsykojkufkml_zpglsvoutvzkgdep_usgrufyvgsbsmbpr_katrrwuhwvunjqor_btngwrpcxoyfbgbc_bxjscjdiowjrkpns_nwxvnfrnlkgqxvhf_ikhyqkvljucgdlag_xibnxsjopmxvflkl_mzplumcfivqcjqnz_jqflcxoxzlbwlxry_fcscvmfepdxrshxe_wlpffwunffklzbuc_emvrlqajjgwzfmle_rhaheurtzrfoqkyq_ifuuhpxmadaysfsx_ncyfvleyzqntpcoo_zeogmyaqccmtvokd_jqppbzebppdnpurn_xixarswxsiwjzgni_ezruwzajsoombphs_hmiqfeizyprielxf_jnaoxljnftymsfey_extgzrxzovlsixnf_yhyfmovvlrwoezsv_ffnybaolppuzpjym_pqowimdiusccaagn_jgceiosiihpjsmnu_hkoexeaopebktngx_njhzuvsygymejqav_yjkgcclgtvushcfk_gmbjxhnkkxlihups_pdlwysadiebsidjz_omrwmgzulfoaqros_ofvvgdezwvcffdcy_otytpuklhxcpxhgd_eyfaosxdauumvlux_mvdthjfstrlqlyuo_mdgdchgnlxaxspdm_bakjezmhbwqxzevd_msakswaphdwaodhg_vjcqscgdbnsxdllh_jjywaovewbuzreoj_nqvplhwacylifvwk_lpwmpixbxysmsign_flcvbpxrchcpbgcb_qjpkeuenenwawlok_bnqkflfmdmntctya_fzsgzpoqixvpsneq_icwfdisutoilejld_relchofohnkwbumi_aljalgdaqwhzhfwr_cahkvnwnbwhodpqs_dnrzeunxiattlvdm_nsmkhlrpwlunppjs_mqqsexlwfqnogwub_tfavelkqrtndpait_ooguafrnmprfxcnz_ntynkiordzxtwrqa_rkkyzlxekqqlkvym_ofxcivdnwcmgfnme_ywotqwbrqxlrnobh_nrbbiypwhrqihvev_flqsjixxtydheufs_lcfrfzypstrqctja_hyzbuzawuzjrynny_exfbywcnstebnvmq_vydzwnbmcihvqrnj_qmwqaaylinzrdmiw_lpxpztpvfggspeun_lhxmqqbracsuyrfm_zgkwsrabaseidbrw_yjlmbhbqsqgszsun_mqfzqtbxtuteabtd_izomzdmcqmfrevwd_iqijrlqurdwrkoln_fxhqzpgoxxjkkhql_oulwontmgrjeopnk_edaigfydjexvzzvj_vjhybiklxpxjqpwc_ypxfbfnpbmqmwtte_xzvcsgasztrxdzud_rpulqmobptfarboo_palacmdijxzzykrf_jmllwukplufohiby_dnswayomusiekfmy_sxbrjqtqgzzwhcfo_lylvndsgbnbqiejm_jaxxhoulxnxnaenr_nblissutfazbcpwn_zmlsjszzldvbiacr_kewojtlchfkclqwk_eqvfjasddggvfame_yibzqlvxtraxpdon_dgnbxsbmdrtyvaac_uoxrcxfimhgtxqhy_xfdxalrwcwudlviq_xmtbdklqptoswpwl_zezyopzdztdjerfl_xuzluhjsqvhytgbc_qdjtmeckispmgzki_phakupesplzmmmvc_gpuoqfffumzszybn_bhywxqkrrlwuebbw_ibvwgoyvelzenkzl_ncohvvbmiekbaksa_fzuvqzvxvdbeirrp_lshtzniokucwojjd_punrduvlnrulkium_gnfpikidnfobrrme_vxkvweekmnvkzgyl_rhydssudkcjlqgxn_cjtqvlaahohcgumo_jwzmfyinsfwecgcb_blpeseqhlzfilpuf_jvtpjkyokzcvagon_qjomincbcobjczpe_ugsyzkzgdhxtmsfz_hleaqgwzqjwajcra_coumfghptpnxvvov_hqpnbupnzwpdvgqd_cpouyodqxgviasem_lljvxeyozckifhfd_huqtnvutdyfgwtwa_yenlveuynmlmmymu_ojdyufkomxiwjmbf_spjzgvcwvzgffjkk_vxykmjhyvmhyssbp_tazdeqggfcjfvwwn_uumwcngwcytvpufx_avovuzkrevloneop_owczrtbnrvjfemkt_hzpugcanaxyvaokj_iishlodnxvjtgzyn_qosdonclrnxirham_eonqlnwevahydddg_ryqmnuikftlxuoqy_whqepbcwabzbthha_vekisvnwhgpyemxr_lrwxzoamnvpnlhap_ywepvqthnorfswjv_evqwvsoazmwyypjy_bgwoojddubppmjxf_jypkfrthzgtyeddi_tynabbhfjzkrqsju_adxstbfqheuqbcuk_gqwqiocdyqoiblrx_ybuddlyuskdlegxv_luwynbsmpgyeqsbr_ltyqgqoyljibqndo_jaedpajzphfybajh_epglnrxofptsqvmy_zjdpxkngfkstxbxh_ekegphcwanoickfu_cqvhuucvejqirvfs_uqudnnqumsqcgefo_qnzunermlnpcfflo_ovyxaniqaawzfuxx_djekxcezjowdhopq_bwtwbmdehrhpjnlk_nilsnlacerweikfa_hyrigsrmsrzcyaus_gvmdmgddduylmxic_ewzovdblhmjgjwsk_ojjfsknlonzguzlq_yjgfruvpjvlvrvvq_cyoryodwyhzwprbv_crsjclrurcquqgut_sjhfhobwtojxcmem_ibxfjudilmdeksea_uqbhdbjoeupyhbcz_uqbxigzxuxgmjgnw_jashafmtzrhswirg_dexiolovaucyooka_czjbwwnlwcoqnoiu_ojigosazigfhttjc_zfiqtgrqbmftknzn_dlzbmvmolssbqlzl_sgmchcurrutdtsmw_scdwjqsdohcdrwry_cgtdvecqwplpprxn_iiplenflfczaktwi_wmgnwfxfcjhyeiqg_giihshowtcatecvl_nqhzfincclumvkaz_kxstpzgdfvepionc_agbhxcijxjxerxyi_hmgfqevgdyvisyvs_tthakmvpowpvhtao_ottalcghygpaafbo_aplvozayycremgqg_dbjxlnaouxqtdpfz_peeyallzjsdvpalc_ndtdjyboixuyhfox_llabnbcobexfoldn_cweuvfnfyumbjvxr_ewkhhepaosalnvkk_pivyiwsiqpwhagyx_auzsnwdcerfttawt_grbfrekupciuzkrt_byfwzadtzrbndluf_lluypxjeljzquptk_pskwsnhqanemtfou_sxvrtqqjdjkfhhrm_ulsmqgmshvijyeqh_qigofesfhekoftkf_zhatniakqtqcxyqa_uuczvylgnxkenqee_mlitvtuxknihmisc_srrtrxdvcokpyfmz_osispuucklxcfkeb_vqhazlaulmnpipql_umkiueljberqhdig_knvpbkbvgoqzwprp_nbsocqikhuvsbloj_wjnpepjkzkednqbm_agbhmytsofuyqcor_gvogzhkkpxyfecko_ardafguxifeipxcn_yiajcskbgykyzzkw_sejunbydztyibnpq_dqrgfggwcnxeiygy_xnqqwilzfbhcweel_jjtifhlvmyfxajqi_gwszrpgpmbpiwhek_kydzftzgcidiohfd_efprvslgkhboujic_kecjdfwqimkzuynx_rildnxnexlvrvxts_dlnhjbqjrzpfgjlk_qluoxmzyhkbyvhub_crydevvrjfmsypbi_dosaftwumofnjvix_pwsqxrfwigeffvef_nzyfmnpwqyygjvfx_iccbckrkxlwjsjat_bmputypderxzrwab_bhuakynbwnlreixb_qmrzfyqjiwaawvvk_juvtixbkwyludftn_zapmjxmuvhuqlfol_paiwrqjhpjavuivm_tsepfbiqhhkbyriz_jpprewufiogxoygk_mmapyxbsugcsngef_pduhmgnepnpsshnh_aetndoqjvqyjrwut_fnfvlorhwpkkemhz_gedfidpwvoeazztl_beclvhospgtowaue_wsclsvthxustmczm_tjbxhnpniuikijhe_rhetyhvfcemponeg_mavonujurprbeexi_argbrpomztrdyasa_bzvtffbtygjxmkvh_maqyqkhsqgzfzvve_seeirbiynilkhfcr_wxmanwnozfrlxhwr_dieulypsobhuvswb_nxevassztkpnvxtb_jclxuynjsrezvlcy_xlolzyvgmwjsbmyf_tguzoeybelluxwxc_fkchoysvdoaasykz_cyynwbfcqpqapldf_rhifmzpddjykktuy_ndvufsyusbxcsotm_txutnzvdsorrixgg_qjoczhukbliojneu_ufhwujotncovjjsz_kclsgsdwcrxsycbr_yscwmlrdaueniiic_nxhivrovpkgsmugb_fdxqfyvwwvgeuqkv_femtamfylysohmpr_amsyzslvyxsoribh_nhmqxncwsonhgbcz_uomqsvcbpthlmcue_kxtfapcqrnjkkslj_xtieihonlfubeync_adpcjqxgydulchgj_cjynnzsmmujsxxpd_neeapmzweidordog_szoivgqyqwnyjsnk_uwgrtzaqezgphdcu_ptpgttqxocjwxohi_fhltebsizfwzpgpf_emmsazsidspkhgnh_dxcprkbcjeqxqzgn_tpxzqwxbzwigdtlt_afsmksnmzustfqyt_xyehnftstacyfpit_vcrfqumhjcmnurlw_rrznpjzcjgnugoch_gbxnzkwsjmepvgzk_jwobshgwerborffm_zmuvfkhohoznmifs_buyuwgynbtujtura_bevncenmpxfyzwtf_hqqtcrhzfsrcutjh_kbpzshllpiowepgc_alspewedcukgtvso_xvsvzzdcgjuvutrw_pmwulqraatlbuski_abuzsiinbueowpqn_oedruzahyfuchijk_avhcuhqqjuqkesoq_azqgplkzsawkvnhb_rjyoydogkzohhcvx_aezxwucqvqxuqotb_kxobnsjvzvenyhbu_nnjoiilshoavzwly_aijttlxjrqwaewgk_cvsaujkqfoixarsw_zngtoacpxcsplgal_qhkxliqtokvepcdv_aixihrtdmxkfvcqw_owbgdgdymxhhnoum_tajsagmruwzuakkd_ckrfduwmsodeuebj_alfdhuijuwyufnne_xpchlkijwuftgmnm_rwcrvgphistiihlg_xdaksnorrnkihreq_akeschycpnyyuiug_rgputhzsvngfuovz_lerknhznuxzdhvre_mqiqmyladulbkzve_csnmupielbbpyops_kwgrwgmhfzjbwxxz_npwtvbslvlxvtjsd_zxleuskblzjfmxgf_hexvporkmherrtrn_rhtdhcagicfndmbm_qhnzyuswqwoobuzz_dpvanjuofrbueoza_kjcqujmnhkjdmrrf_gholddsspmxtpybg_jihlvyqdyzkshfsi_zuviqmuqqfmtneur_kzexjowatvkohrtx_wgijnfhibsiruvnl_zevkrkmhsxmicijb_khxrcteqourjvoxa_ylpxlkcnenbxxtta_zrfsvctbojjkpvtw_nlzbudxibnmcrxbt_cqnscphbicqmyrex_ywvdohheukipshcw_riwatbvjqstubssf_idlztqqaxzjiyllu_sdpdgzemlqtizgxn_rjtbovqlgcgojyjx_fnfrfwujmjwdrbdr_osnppzzmrpxmdhtj_ljhwngclvydkwyoe_chwqkrkzrvjwarat_jmydkwpibkvmqlgs_zvhfmbxnlxtujpcz_jsnhsphowlqupqwj_fzhkkbpasthopdev_jerntjdsspdstyhf_gctwmaywbyrzwdxz_xemeaiuzlctijykr_xulrqevtbhplmgxc_yfejfizzsycecqpu_gboxrvvxyzcowtzm_lpvhcxtchwvpgaxp_wdiwucbdyxwnjdqf_qgwoqazzjlvnjrwj_prtlnkakjfqcjngn_fagvxsvjpuvqxniz_xacmxveueaakfbsm_ginvtonnfbnugkpz_qpvggsppewfzvwin_reoqnlzruyyfraxa_kolwtqhifjbbuzor_vrkcywvdhdprztww_ngdvyfmvjqhbzbxt_rooxeoilqzqjunmp_efxmdprtogtxgyqs_qrhjuqndgurcmwgu_ouitjprueefafzpl_kirdwcksqrbwbchp_fpumsmogojuywezo_lgjrgykywugzjees_xigioqcpjabpbdas_ewkhuprpqzikmeop_fgrgxsqeducigxvr_bclkursnqkzmjihl_jozidniwvnqhvsbc_oghcilcyozrmmpta_xbgmaungzcpasapi_iqowypfiayzbcvhv_opdehgwdgkocrgkf_zfzvdjeinlegcjba_vhakxvlcayuzukap_xyradgyiebpevnwe_eamhtflgedwyshkn_igteqdgchjeulfth_kwsfkigxzpbgdxod_vapnpsbdboiewpzp_wbuqhjsngxpqshen_vxxilouxuytitwgm_cpnwlkwnkeanqnet_wdmbtqvvlowftvgb_wjtmcecpyqzwpbqg_jnxmoxdhvsphcdeg_wabxfxpotoywwodn_mwbsoxzlqpqobvvh_coktshbyzjkxnwlt_rzhnggpslwzvyqrp_dgzuqbzarbutlkfx_wunajaiiwgijfvjh_uotdbcgmsvbsfqlb_kxdtlgmqbccjqldb_ngmjzjwvwbegehfr_cvpsabqfpyygwncs_wqluvqlhdhskgmzj_rbveperybfntcfxs_fbmoypqdyyvqyknz_zxpgzwnvmuvkbgov_yexcyzhyrpluxfbj_ltqaihhstpzgyiou_munhsdsfkjebdicd_plecvjctydfbanep_kjrxnnlqrpcieuwx_zbcdtcqakhobuscf_kgovoohchranhmsh_llxufffkyvuxcmfx_tgaswqyzqopfvxtw_kojcqjkdpzvbtjtv_xggdlkmkrsygzcfk_vvitpsnjtdqwyzhh_gcqjuwytlhxsecci_vbsghygcsokphnrg_vejqximdopiztjjm_hudqtwmwkviiuslp_vwswfvpcwwpxlyry_gxmfiehdxptweweq_qjmekjdcedfasopf_pqyxdxtryfnihphf_felnavctjjojdlgp_hbimufguekgdxdac_dhxhtnqgfczywxlr_pssottpdjxkejjrh_edieanguabapxyig_sciinanyqblrbzbb_irxpsorkpcpahiqi_qsxecaykkmtfisei_ivfwlvxlbnrzixff_hqxzzfulfxpmivcw_vvbpaepmhmvqykdg_cetgicjasozykgje_wuetifzdarhwmhji_gaozwhpoickokgby_eldnodziomvdfbuv_favpaqktqaqgixtv_twbcobsayaecyxvu_lzyzjihydpfjgqev_wnurwckqgufskuoh_fxogtycnnmcbgvqz_aetositiahrhzidz_dyklsmlyvgcmtswr_ykaxtdkjqevtttbx_kfmnceyxyhiczzjm_nnizopcndipffpko_yjmznhzyfinpmvkb_sljegcvvbnjhhwdd_zmkeadxlwhfahpwg_rwvcogvegcohcrmx_aguqwrfymwbpscau_vlusytjagzvsnbwe_smvzhburcgvqtklh_rfuprvjkhazrcxpv_megqlnoqmymcrclc_gvldhkewtmlwqvqv_awynhvtyziemnjoa_voprnvtnzspfvpeh_dhlguqwmunbbekih_goayirdhnjrfuiqi_eoghydfykxdslohz_chpippjykogxpbxq_hqbycjweqczwjwgf_pvefsrvwumrlvhmt_eghwdovaynmctktk_crwkxoucibumzawc_bzbtahvhkdigvvtj_bnbptgihhfubxhho_ddqmbwyfmfnjjaro_gvtswqyzazihctif_vmqctjpgadxztqqb_dgnndowtpeooaqqf_sxdvctfdtalufxty_ylgeexosibsmmckw_sxplpyskbpqnojvw_coarhxtsvrontyeg_fyoaurggjupvzvlv_jlyrkqsiwuggvjem_uwbsjoxonreuucyi_gihuqvwxovbgokes_dxzaaxupbcgnxcwf_gidrgmvyrlqqslve_csflmlvqmonoywpx_jkxkpixlythlacnk_ejkarcdkdslldugv_dbzmsusevohhjkmr_cbrqzualjpdtworc_kpgidqlmcbpfmmwu_zwghjuofexfowqam_ncdlxmcrsmsocetz_kfprzqacefifjkbd_swwzivrxulkhvldc_wgqejhigbjwunscp_rsstnwcyybfauqxu_qhngfxyhdqopyfgk_zrndpyyejsmqsiaj_xxknxwpvafxiwwjc_mmaahwgoiwbxloem_tabacndyodmpuovp_yriwomauudscvdce_duvyscvfidmtcugl_mgipxnqlfpjdilge_imeeqcdetjuhfjnw_dvkutrdofpulqkyh_jefvtlktxegpmbya_iyzudqgpvlzjfydh_giohapxnpaqayryd_qheqdprmnqlpztls_rdxhijmzegxkotoq_hdnmaspumdwnrcdz_wafpbgehbuzdgsnc_tbtrfztsferdmhsy_vusndcyjngtkrtmk_ilqblestzxebcifh_urfgjbjgzlrfsdlv_aptcdvpsqwleqttn_bigczjvzokvfofiw_zjnjeufonyqgkbpx_trcdebioegfqrrdi_jrdvdriujlmbqewt_jqrcmuxpwurdhaue_yjlermsgruublkly_zwarvgszuqeesuwq_xthhhqzwvqiyctvs_mzwwaxnbdxhajyyv_nclsozlqrjvqifyi_gcnyqmhezcqvksqw_deuakiskeuwdfxwp_tclkbhqqcydlgrrl_qbpndlfjayowkcrx_apjhkutpoiegnxfx_oaupiimsplsvcsie_sdmxrufyhztxzgmt_ukfoinnlbqrgzdeh_azosvwtcipqzckns_mydyeqsimocdikzn_itfmfjrclmglcrkc_swknpgysfscdrnop_shyyuvvldmqheuiv_tljrjohwhhekyhle_dayinwzuvzimvzjw_qgylixuuervyylur_klqqaiemurawmaaz_hdmzgtxxjabplxvf_xiivzelzdjjtkhnj_ktgplkzblgxwrnvo_gvbpyofzodnknytd_lqhlmnmhakqeffqw_ltzdbngrcxwuxecy_obxnfjeebvovjcjz_zexpwallpocrxpvp_tjpkkmcqbbkxaiak_qiedfixxgvciblih_qcxkhghosuslbyih_gnsfidwhzaxjufgm_xrghwgvyjakkzidw_tftftwedtecglavz_wquqczzkzqrlfngr_twibtkijpvzbsfro_bmplypdsvzuhrjxp_zanrfmestvqpwbuh_zonrhfqowyimcukm_kpvajjfmqpbhrjma_kujzluicngigjbtp_iusguantsrwxdjal_kwxeuylcnszswahw_visdhnkobxnemldu_rogeadmmaicwtabl_pxqycifbgevqudvs_osaiozyvlyddylqr_vffjxrolrpuxcatx_jbmsetccdrywssjd_qgxyhjfpbfifmvgc_npejgalglldxjdhs_mbbtqgmttastrlck_whapaqwdtpkropek_dulbdboxazfyjgkg_xaymnudlozbykgow_lebvqmxeaymkkfoy_bmicnfuubkregouj_dieatyxxxlvhneoj_yglaapcsnsbuvrva_bbpjaslqpzqcwkpk_xehuznbayagrbhnd_ikqmeovaurmqfuvr_ylyokwuzxltvxmgv_hqtfinrkllhqtoiz_pjmhtigznoaejifx_fqdbmowkjtmvvrmx_uvqtqfoulvzozfxv_rpajajukuxtchrjd_sznucejifktvxdre_ufvibsmoushmjbne_xirdqoshngthfvax_iafpkddchsgdqmzl_vmualmlduipvykzh_fnmuahmblwyceejb_ilsaapnswfoymiov_lenvylifraahaclv_cukqxlipuyxedqfh_zgwecslpniqvtvuz_cdcdfpsxuyrhsmag_dszjinhantnxgqra_ioimwotsgnjeacgt_dqcymnvjystbynhp_yibaudyfefbfgunx_cabslcvunjavqkbf_goymzvmgkvlsmugf_zxteiitpthzskjjx_agnxcnaqhjhlurzs_cvmgyxhhnykuxbmb_cgqmjexydmvgwxpp_sygjajofieojiuna_clpvxbrbjvqfbzvu_cbntswqynsdqnhyv_bztpbtwbefiotkfa_pnxccbgajvhyeybu_asyzrvgzumtuissa_facjyblvcqqginxa_rvwnucnbsvberxuv_ghrbeykzrxclasie_ekujtselepgjtaql_krtrzsmduhsifyiw_ticjswvsnyrwhpnt_clmjhsftkfjzwyke_lbxlcixxcztddlam_xhfeekmxgbloguri_azxqwlucwhahtvep_kitdjrwmockhksow_keznwwcusgbtvfrs_ljvzxoywcofgwajj_vebjnhnkcfzbhrcw_eqfcxkavstxcuels_ldattkyawjrvcido_bsqqeilshcwtqyil_foqqsxahfiozcqrw_liswfmuhzfbyzjhf_sulbdcyzmolapfbs_zuggzkelwxjpsgxb_betioxrgtnhpivcw_xmtbixstdipibhgs_ttvurgqmulryyaji_viobnljznzppfmxw_qlzabfopydtxrlet_tusvydegfxhaxolk_thoufvvfjferxhwp_cfyyzppfarjiilbs_jwmhxtgafkkgseqs_pqwuuaxbeklodwpt_vndyveahdiwgkjyx_ssrjgasfhdouwyoh_thbavfcisgvvyekf_yjdvxmubvqadgypa_tlbmcxaelkouhsvu_bonohfnlboxiezzr_rktlxcbkhewyvcjl_rsmoutcbcssodvsc_qszdratuxcrhsvoh_eypyfahpuzqwzwhi_yhkrleqmqlmwdnio_vpnvxusvmngsobmq_hkzyhopvxrsimzys_dblriiwnrvnhxykl_xkriqxkrprjwpncs_rcymltrbszhyhqti_mzbvneplsnpiztzn_vkqtnptgbqefvfoc_nwdtfiaozkcjtlax_crximadpvdaccrsm_lrbajafxwwnxvbei_rbexzesrytpwwmjf_stxwjarildpnzfpg_btamaihdivrhhrrv_acqbucebpaulpotl_dkjhzghxxtxgdpvm_rsbzwsnvlpqzyjir_mizypbwvpgqoiams_nvrslorjpqaasudn_wvexcpzmconqkbvk_rfwfumhjwzrvdzam_eaghdaqorkhdsmth_gtuntmpqaivosewh_nzlsmdgjrigghrmy_dhuvxwobpzbuwjgk_kkcuvbezftvkhebf_aeediumxyljbuyqu_rfkpqeekjezejtjc_wkzasuyckmgwddwy_eixpkpdhsjmynxhi_elrlnndorggmmhmx_ayxwhkxahljoxggy_mtzvvwmwexkberaw_evpktriyydxvdhpx_otznecuqsfagruls_vrdykpyebzyblnut_cnriedolerlhbqjy_uajaprnrrkvggqgx_xdlxuguloojvskjq_mfifrjamczjncuym_otmgvsykuuxrluky_oiuroieurpyejuvm"
        stringList = entryString.split('_')
        puzzleNumber = input('Enter the puzzle Number:')
        if puzzleNumber == 1:
            for string in stringList:
                #check for three vowels
                match = ThreeVowelRe.search(string)
                if match:
                    pass
                    #print("found three vowels")
                else:
                    print('There arent three vowels..')
                    continue

                #check for two letters in a row
                match = TwoInARowRe.search(string)
                if match:
                    pass
                    #print("it's a match")
                else:
                    print('There arent two letters in a row...')
                    continue

                #check for dissallowed characters
                match = DisallowedStrings.search(string)
                if match:
                    print('Found illegal string...')
                    continue
                else:
                    niceStrings = niceStrings+1
            print('Number of NiceStrings : '+str(niceStrings))
        else:
            for string in stringList:
                print(string)
                match = MatchWithOneBetween.search(string)
                if match:
                    print('one between found')
                    pass
                else:
                    continue
                    
                match = MatchTwoPairs.search(string)
                if match:
                    print('pairs found:'+match.group(0));
                    niceStrings = niceStrings+1
            print('Number of NiceStrings : '+str(niceStrings))
            
            
            
    elif command == '6':
        import re
        numOfLights = list(range(1000))
        lightArray = {}
        for x in numOfLights:
            lightArray[x] = {}
            for y in numOfLights:
                lightArray[x][y] = 0
        inputString = "turn on 887,9 through 959,629_turn on 454,398 through 844,448_turn off 539,243 through 559,965_turn off 370,819 through 676,868_turn off 145,40 through 370,997_turn off 301,3 through 808,453_turn on 351,678 through 951,908_toggle 720,196 through 897,994_toggle 831,394 through 904,860_toggle 753,664 through 970,926_turn off 150,300 through 213,740_turn on 141,242 through 932,871_toggle 294,259 through 474,326_toggle 678,333 through 752,957_toggle 393,804 through 510,976_turn off 6,964 through 411,976_turn off 33,572 through 978,590_turn on 579,693 through 650,978_turn on 150,20 through 652,719_turn off 782,143 through 808,802_turn off 240,377 through 761,468_turn off 899,828 through 958,967_turn on 613,565 through 952,659_turn on 295,36 through 964,978_toggle 846,296 through 969,528_turn off 211,254 through 529,491_turn off 231,594 through 406,794_turn off 169,791 through 758,942_turn on 955,440 through 980,477_toggle 944,498 through 995,928_turn on 519,391 through 605,718_toggle 521,303 through 617,366_turn off 524,349 through 694,791_toggle 391,87 through 499,792_toggle 562,527 through 668,935_turn off 68,358 through 857,453_toggle 815,811 through 889,828_turn off 666,61 through 768,87_turn on 27,501 through 921,952_turn on 953,102 through 983,471_turn on 277,552 through 451,723_turn off 64,253 through 655,960_turn on 47,485 through 734,977_turn off 59,119 through 699,734_toggle 407,898 through 493,955_toggle 912,966 through 949,991_turn on 479,990 through 895,990_toggle 390,589 through 869,766_toggle 593,903 through 926,943_toggle 358,439 through 870,528_turn off 649,410 through 652,875_turn on 629,834 through 712,895_toggle 254,555 through 770,901_toggle 641,832 through 947,850_turn on 268,448 through 743,777_turn off 512,123 through 625,874_turn off 498,262 through 930,811_turn off 835,158 through 886,242_toggle 546,310 through 607,773_turn on 501,505 through 896,909_turn off 666,796 through 817,924_toggle 987,789 through 993,809_toggle 745,8 through 860,693_toggle 181,983 through 731,988_turn on 826,174 through 924,883_turn on 239,228 through 843,993_turn on 205,613 through 891,667_toggle 867,873 through 984,896_turn on 628,251 through 677,681_toggle 276,956 through 631,964_turn on 78,358 through 974,713_turn on 521,360 through 773,597_turn off 963,52 through 979,502_turn on 117,151 through 934,622_toggle 237,91 through 528,164_turn on 944,269 through 975,453_toggle 979,460 through 988,964_turn off 440,254 through 681,507_toggle 347,100 through 896,785_turn off 329,592 through 369,985_turn on 931,960 through 979,985_toggle 703,3 through 776,36_toggle 798,120 through 908,550_turn off 186,605 through 914,709_turn off 921,725 through 979,956_toggle 167,34 through 735,249_turn on 726,781 through 987,936_toggle 720,336 through 847,756_turn on 171,630 through 656,769_turn off 417,276 through 751,500_toggle 559,485 through 584,534_turn on 568,629 through 690,873_toggle 248,712 through 277,988_toggle 345,594 through 812,723_turn off 800,108 through 834,618_turn off 967,439 through 986,869_turn on 842,209 through 955,529_turn on 132,653 through 357,696_turn on 817,38 through 973,662_turn off 569,816 through 721,861_turn on 568,429 through 945,724_turn on 77,458 through 844,685_turn off 138,78 through 498,851_turn on 136,21 through 252,986_turn off 2,460 through 863,472_turn on 172,81 through 839,332_turn on 123,216 through 703,384_turn off 879,644 through 944,887_toggle 227,491 through 504,793_toggle 580,418 through 741,479_toggle 65,276 through 414,299_toggle 482,486 through 838,931_turn off 557,768 through 950,927_turn off 615,617 through 955,864_turn on 859,886 through 923,919_turn on 391,330 through 499,971_toggle 521,835 through 613,847_turn on 822,787 through 989,847_turn on 192,142 through 357,846_turn off 564,945 through 985,945_turn off 479,361 through 703,799_toggle 56,481 through 489,978_turn off 632,991 through 774,998_toggle 723,526 through 945,792_turn on 344,149 through 441,640_toggle 568,927 through 624,952_turn on 621,784 through 970,788_toggle 665,783 through 795,981_toggle 386,610 through 817,730_toggle 440,399 through 734,417_toggle 939,201 through 978,803_turn off 395,883 through 554,929_turn on 340,309 through 637,561_turn off 875,147 through 946,481_turn off 945,837 through 957,922_turn off 429,982 through 691,991_toggle 227,137 through 439,822_toggle 4,848 through 7,932_turn off 545,146 through 756,943_turn on 763,863 through 937,994_turn on 232,94 through 404,502_turn off 742,254 through 930,512_turn on 91,931 through 101,942_toggle 585,106 through 651,425_turn on 506,700 through 567,960_turn off 548,44 through 718,352_turn off 194,827 through 673,859_turn off 6,645 through 509,764_turn off 13,230 through 821,361_turn on 734,629 through 919,631_toggle 788,552 through 957,972_toggle 244,747 through 849,773_turn off 162,553 through 276,887_turn off 569,577 through 587,604_turn off 799,482 through 854,956_turn on 744,535 through 909,802_toggle 330,641 through 396,986_turn off 927,458 through 966,564_toggle 984,486 through 986,913_toggle 519,682 through 632,708_turn on 984,977 through 989,986_toggle 766,423 through 934,495_turn on 17,509 through 947,718_turn on 413,783 through 631,903_turn on 482,370 through 493,688_turn on 433,859 through 628,938_turn off 769,549 through 945,810_turn on 178,853 through 539,941_turn off 203,251 through 692,433_turn off 525,638 through 955,794_turn on 169,70 through 764,939_toggle 59,352 through 896,404_toggle 143,245 through 707,320_turn off 103,35 through 160,949_toggle 496,24 through 669,507_turn off 581,847 through 847,903_turn on 689,153 through 733,562_turn on 821,487 through 839,699_turn on 837,627 through 978,723_toggle 96,748 through 973,753_toggle 99,818 through 609,995_turn on 731,193 through 756,509_turn off 622,55 through 813,365_turn on 456,490 through 576,548_turn on 48,421 through 163,674_turn off 853,861 through 924,964_turn off 59,963 through 556,987_turn on 458,710 through 688,847_toggle 12,484 through 878,562_turn off 241,964 through 799,983_turn off 434,299 through 845,772_toggle 896,725 through 956,847_turn on 740,289 through 784,345_turn off 395,840 through 822,845_turn on 955,224 through 996,953_turn off 710,186 through 957,722_turn off 485,949 through 869,985_turn on 848,209 through 975,376_toggle 221,241 through 906,384_turn on 588,49 through 927,496_turn on 273,332 through 735,725_turn on 505,962 through 895,962_toggle 820,112 through 923,143_turn on 919,792 through 978,982_toggle 489,461 through 910,737_turn off 202,642 through 638,940_turn off 708,953 through 970,960_toggle 437,291 through 546,381_turn on 409,358 through 837,479_turn off 756,279 through 870,943_turn off 154,657 through 375,703_turn off 524,622 through 995,779_toggle 514,221 through 651,850_toggle 808,464 through 886,646_toggle 483,537 through 739,840_toggle 654,769 through 831,825_turn off 326,37 through 631,69_turn off 590,570 through 926,656_turn off 881,913 through 911,998_turn on 996,102 through 998,616_turn off 677,503 through 828,563_turn on 860,251 through 877,441_turn off 964,100 through 982,377_toggle 888,403 through 961,597_turn off 632,240 through 938,968_toggle 731,176 through 932,413_turn on 5,498 through 203,835_turn on 819,352 through 929,855_toggle 393,813 through 832,816_toggle 725,689 through 967,888_turn on 968,950 through 969,983_turn off 152,628 through 582,896_turn off 165,844 through 459,935_turn off 882,741 through 974,786_turn off 283,179 through 731,899_toggle 197,366 through 682,445_turn on 106,309 through 120,813_toggle 950,387 through 967,782_turn off 274,603 through 383,759_turn off 155,665 through 284,787_toggle 551,871 through 860,962_turn off 30,826 through 598,892_toggle 76,552 through 977,888_turn on 938,180 through 994,997_toggle 62,381 through 993,656_toggle 625,861 through 921,941_turn on 685,311 through 872,521_turn on 124,934 through 530,962_turn on 606,379 through 961,867_turn off 792,735 through 946,783_turn on 417,480 through 860,598_toggle 178,91 through 481,887_turn off 23,935 through 833,962_toggle 317,14 through 793,425_turn on 986,89 through 999,613_turn off 359,201 through 560,554_turn off 729,494 through 942,626_turn on 204,143 through 876,610_toggle 474,97 through 636,542_turn off 902,924 through 976,973_turn off 389,442 through 824,638_turn off 622,863 through 798,863_turn on 840,622 through 978,920_toggle 567,374 through 925,439_turn off 643,319 through 935,662_toggle 185,42 through 294,810_turn on 47,124 through 598,880_toggle 828,303 through 979,770_turn off 174,272 through 280,311_turn off 540,50 through 880,212_turn on 141,994 through 221,998_turn on 476,695 through 483,901_turn on 960,216 through 972,502_toggle 752,335 through 957,733_turn off 419,713 through 537,998_toggle 772,846 through 994,888_turn on 881,159 through 902,312_turn off 537,651 through 641,816_toggle 561,947 through 638,965_turn on 368,458 through 437,612_turn on 290,149 through 705,919_turn on 711,918 through 974,945_toggle 916,242 through 926,786_toggle 522,272 through 773,314_turn on 432,897 through 440,954_turn off 132,169 through 775,380_toggle 52,205 through 693,747_toggle 926,309 through 976,669_turn off 838,342 through 938,444_turn on 144,431 through 260,951_toggle 780,318 through 975,495_turn off 185,412 through 796,541_turn on 879,548 through 892,860_turn on 294,132 through 460,338_turn on 823,500 through 899,529_turn off 225,603 through 483,920_toggle 717,493 through 930,875_toggle 534,948 through 599,968_turn on 522,730 through 968,950_turn off 102,229 through 674,529"
        inputCommands = inputString.split('_')
        puzzleNumber6 = input('Enter the puzzle Number:')
        print(puzzleNumber6)
        for commandString in inputCommands:
            command = re.search("([a-z]*.[a-z]*)", commandString)
            beginningCoor = re.search("([0-9]*,[0-9]*)", commandString)
            endCoor = re.search("through ([0-9]*,[0-9]*)", commandString)
            begCoorArray = beginningCoor.group(0).split(',');
            endCoorArray = endCoor.group(1).split(',');

            XRange = list(range(int(begCoorArray[0]), int(endCoorArray[0])+1))
            YRange = list(range(int(begCoorArray[1]), int(endCoorArray[1])+1))
            for x in XRange:
                for y in YRange:
                    
                    if command.group(0) == 'turn on':
                        if puzzleNumber6 == '1':
                            lightArray[x][y] = 1
                        if puzzleNumber6 == '2':
                            lightArray[x][y] = lightArray[x][y]+1
                    if command.group(0) == 'turn off':
                        if puzzleNumber6 == '1':
                            lightArray[x][y] = 0
                        if puzzleNumber6 == '2':
                            lightArray[x][y] = lightArray[x][y]-1
                            if(lightArray[x][y] < 0):
                                lightArray[x][y] = 0
                    if command.group(0) == 'toggle ':
                        if puzzleNumber6 == '1':
                            if lightArray[x][y] == 1:
                                lightArray[x][y] = 0
                            else:
                                lightArray[x][y] = 1
                        if puzzleNumber6 == '2':
                            lightArray[x][y] = lightArray[x][y]+2
                        
        
        TurnedOnLights = 0;
        TotalBrightness = 0
        for x in lightArray:
            for y in lightArray[x]:
                if puzzleNumber6 == '1' and lightArray[x][y] == 1:
                    TurnedOnLights = TurnedOnLights+1
                elif puzzleNumber6 == '2':
                    TotalBrightness = TotalBrightness+lightArray[x][y]
        print('Number of Turned on Lights:'+str(TurnedOnLights))
        print('Total birghtness:'+str(TotalBrightness))
        
        
        
    elif command == '7':
        def isInt(s):
            try: 
                int(s)
                return True
            except ValueError:
                return False
        
        print('Reading in from file.')
        #get the puzzle input
        commandSequence = {}
        inputFile = open('Input/Day7.txt', 'r')
        commandList = inputFile.read()
        commandList = commandList.split("\n")
        i = 0
        for command in commandList:
            commandSequence[i] = command
            i = i+1
        inputFile.close()
        print('Finished reading file.')

        print('Beginning the tokenization.')
        print(commandSequence)
        wireList = {}
        #split each line into a list
        for key in commandSequence:
            line = commandSequence[key]
            commandSequence[key] = line.split(' ')
            #make a dictionary of all wires
            for token in commandSequence[key]:
                if token != 'NOT' and token != 'LSHIFT' and token != 'OR' and token != 'RSHIFT' and token != 'AND' and token != '->' and not isInt(token):
                    if token not in wireList:
                        wireList[token] = 'unknown'
        wireList['b'] = '3176'
        print('Finished tokenizing the commands and building wirelist.')


        print('Starting main process loop...')
        #now we loop over each command row, when we hit an assignment or an equation 
        #with known values(from wireList) then we calculate the value and save it
        solved  = 0
        todrop = []
        try:
            while solved == 0:

                print('Removing previously processed gates')

                for keyToDrop in todrop:
                    del commandSequence[keyToDrop]
                todrop = []#clear the todrop array
                print('Beginning new processing pass. '+ str(len(commandSequence))+' gates left.')
                for key in commandSequence:
                    line = commandSequence[key]
                    print(line)
                    #handle simple assignment cases like:
                    #line['1', '->', 'a']
                    if len(line) == 3:
                        if isInt(line[0]) == False and wireList[line[0]] != 'unknown':
                            line[0] = wireList[line[0]]
                        if isInt(line[0]) and wireList[line[2]] == 'unknown':
                            wireList[line[2]] = line[0]
                            print('Setting ' + str(line[2])+' to '+str(line[0]))
                            todrop.append(key)
                        elif wireList[line[2]] != 'unknown':
                            todrop.append(key)

                    if len(line) == 4 and line[0] == 'NOT':
                        if isInt(line[1]) == False and wireList[line[1]] != 'unknown':
                            line[1] = wireList[line[1]]
                        if isInt(line[1]) and wireList[line[3]] == 'unknown':
                            wireList[line[3]] =  ~int(line[1])
                            todrop.append(key)
                        elif wireList[line[3]] != 'unknown':
                            todrop.append(key)
                            
                    if len(line) == 5:
                        if isInt(line[0]) == False and wireList[line[0]] != 'unknown':
                            line[0] = wireList[line[0]]
                        if isInt(line[2]) == False and wireList[line[2]] != 'unknown':
                            line[2] = wireList[line[2]]
                        if isInt(line[0]) and isInt(line[2]) and wireList[line[4]] == 'unknown':
                            if line[1] == 'LSHIFT':
                                wireList[line[4]] = int(line[0])<<int(line[2])
                                print('Setting ' + str(line[4])+' to ' +str(line[0])+'(LSHIFT)'+str(line[2])+'='+str(wireList[line[4]]))
                                todrop.append(key)
                            if line[1] == 'RSHIFT':
                                wireList[line[4]] = int(line[0])>>int(line[2])
                                print('Setting ' + str(line[4])+' to ' +str(line[0])+'(RSHIFT)'+str(line[2])+'='+str(wireList[line[4]]))
                                todrop.append(key)
                            if line[1] == 'AND':
                                wireList[line[4]] = int(line[0])&int(line[2])
                                print('Setting ' + str(line[4])+' to ' +str(line[0])+'(AND)'+str(line[2])+'='+str(wireList[line[4]]))
                                todrop.append(key)
                            if line[1] == 'OR':
                                wireList[line[4]] = int(line[0])|int(line[2])
                                print('Setting ' + str(line[4])+' to ' +str(line[0])+'(OR)'+str(line[2])+'='+str(wireList[line[4]]))
                                todrop.append(key)
                        elif wireList[line[4]] != 'unknown':
                            todrop.append(key)
                    if isInt(wireList['a']):
                        solved = 1
                        print(wireList)
                        print('Value of a is:'+str(wireList['a']))
        except Exception as e:
            print('Exception occured:'+e)
            
            
    elif command == '8':
        import binascii
        
        puzzleNumber = input('Which Puzzle number?')
        
        runTestCase = input("Run the test case?(y/n):")
        if(runTestCase == 'y' or runTestCase == 'Y'):
            file = open('TestCase/Day8.txt', 'r')
        if(runTestCase == 'n' or runTestCase == 'N'):
            file = open('Input/Day8.txt', 'r')
        firstReading = file.read()
        
        strForReading = firstReading
        strForReading = strForReading.replace("\n", '')
        fileLength = len(strForReading)
        lines = firstReading.split("\n")
        condensedLine = ''
        
        if(puzzleNumber == '1'):
            for line in lines:
                line = line[1:len(line)-1]
                condensedString = ''
                interpretSlash = False
                interpretHex = False
                hexBuffer = ''
                for i in list(range(len(line))):
                    char = line[i]
                    if interpretHex != False:
                        hexBuffer = str(hexBuffer)+str(char)
                        interpretHex = interpretHex-1
                        if interpretHex == 0:
                            char =  'a'#it doesn't matter what the hex character is just stick something in
                            condensedString = condensedString+str(char)
                            interpretHex = False
                    elif interpretSlash == True:
                        if(char == 'x'):
                            interpretHex = 2
                        else:
                            condensedString = condensedString+char
                        interpretSlash = False
                    elif(char == "\\"):
                        interpretSlash = True
                        continue
                    else:
                        condensedString = condensedString+char
                condensedLine = condensedLine+condensedString
            print(fileLength)
            print(len(condensedLine))
            print('The difference between the file and string is:'+str(fileLength-len(condensedLine)))
        else:
            for line in lines:
                line = line[1:len(line)-1]
                condensedString = '"\\"'
                for i in list(range(len(line))):
                    char = line[i]
                    if(char == "\\"):
                        condensedString = condensedString+'\\'+'\\'
                        continue
                    elif(char == '"'):
                        condensedString = condensedString+'\\'+char
                        continue
                    else:
                        condensedString = condensedString+char
                print(condensedString+'\\""')
                condensedLine = condensedLine+condensedString+'\\""'
            print(fileLength)
            print('The condensedLine has '+str(len(condensedLine))+' chars(in this puzzle this is actually an expanded string.)')
            print('The difference between the file and string is:'+str(len(condensedLine)-fileLength))
        
        file.close()
        
    elif command == '9':
        import itertools
        
        print('This Day 9 solution solves both puzzle 1 and 2 simultaneously.')
        
        file = open('Input/Day9.txt', 'r')
        inputText = file.read()
        
        lines = inputText.split('\n')
        cachedDistance = {}
        for line in lines:
            words = line.split(' ')
            #build the cached distance dictionary
            for i in [0, 2]:
                if words[i] not in cachedDistance.keys():
                    for locKey, locDict in cachedDistance.items():
                        if words[i] not in locDict:
                            locDict[words[i]] = 0
                    cachedDistance[words[i]] = {el:0 for el in cachedDistance.keys()}
        for line in lines: #populate the cachedDistance table
            words = line.split(' ')
            cachedDistance[words[0]][words[2]] = words[4]
            cachedDistance[words[2]][words[0]] = words[4]
        print(cachedDistance)
        
        locList = cachedDistance.keys()
        
        permutationList = itertools.permutations(locList, 8)
        permutationList = [x for x in permutationList]
        currLowestDist = 1000
        currHighestDist = 0
        for permut in permutationList:
            currDist = 0
            i = 0
            for stop in permut:
                if i == 0:
                    i += 1
                    continue
                currDist = currDist+int(cachedDistance[stop][permut[i-1]])
                i += 1
            if currDist < currLowestDist:
                currLowestDist = currDist
            if currDist > currHighestDist:
                currHighestDist = currDist
        print('Lowest possible distance is:'+str(currLowestDist))
        print('Highest possible distance is:'+str(currHighestDist))
        
        
        
    elif command == '10':
        string = input('Enter your starting number:')
        
        recursions = 50
        while recursions > 0:
            print('On recursion:'+str(recursions))
            currentChar = ''
            currCharCount = 1
            newString = ''
            for i in list(range(len(string))):
                if i == 0:
                    currentChar = string[i]
                    continue
                if string[i] == currentChar:
                    currCharCount += 1
                else:
                    newString = newString+str(currCharCount)+string[i-1]
                    currentChar = string[i]
                    currCharCount = 1
                if i == len(string)-1:
                    newString = newString+str(currCharCount)+string[i]
            print('old string:'+string)
            print('new string:'+newString)
            string = newString
            recursions -= 1
        print('Length of string after 40 iterations is:'+str(len(string)))
    elif command == '11':
        import Day11
            
print('Exiting script...')
SystemExit.mro()
