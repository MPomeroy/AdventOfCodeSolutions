# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$9-Jan-2016 6:56:07 PM$"

def main():
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
        
main()