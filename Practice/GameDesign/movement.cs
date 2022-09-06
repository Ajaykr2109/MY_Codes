using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;



public class ballgame : MonoBehaviour
{

    Rigidbody rb;
    public int speed;
    int score;
    public TextMeshProUGUI txt;
    public TextMeshProUGUI txtQ;
    float minutes;
    float seconds;

    float timer;


    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        score = 0;
        timer = 60.0f;
    }

        // Update is called once per frame
        void FixedUpdate()
        {
            float x = Input.GetAxis("Horizontal");
            float z = Input.GetAxis("Vertical");

            Vector3 v = new Vector3(x, 0.0f, z);
            rb.AddForce(v * speed);
            timer = timer - Time.deltaTime;
            timer = timer / 60;
            timer = timer % 60;

            txtQ.text = "Timer :" + timer.ToString();


        }




        void OnTriggerEnter(Collider other)
        {
            if (other.gameObject.CompareTag("PICK"))
            {
                Debug.Log("hello");
                other.gameObject.SetActive(false);

            }
        }



        void OnCollisionEnter(Collision other)
        {
            if (other.gameObject.CompareTag("PICK"))
            {
                other.gameObject.SetActive(false);
                score = score + 1;
                Debug.Log(score);
                txt.text = "score :" + score.ToString();

                /* if(score>=4)
                 {
                     txt.text = "you win";
                     UnityEditor.EditorApplication.isPlaying = false;

                 }






                 */

                GetComponent<Renderer>().material.color = Color.gray;


            }


        }



    }